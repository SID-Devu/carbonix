from flask import Flask, render_template, jsonify, request
from data import PROJECTS, PORTFOLIO, TRANSACTIONS, MARKET_STATS, PRICE_HISTORY

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("dashboard.html", stats=MARKET_STATS, transactions=TRANSACTIONS[:10], projects=PROJECTS)


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/project/<project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        return "Project not found", 404
    return render_template("project_detail.html", project=project)


@app.route("/marketplace")
def marketplace():
    return render_template("marketplace.html", projects=PROJECTS, transactions=TRANSACTIONS[:20])


@app.route("/portfolio")
def portfolio():
    holdings = []
    total_value = 0
    total_invested = 0
    total_tons = 0
    for h in PORTFOLIO:
        proj = next((p for p in PROJECTS if p["id"] == h["project_id"]), None)
        if proj:
            current_value = h["tons_held"] * proj["price_per_ton"]
            invested = h["tons_held"] * h["avg_price"]
            gain = current_value - invested
            holdings.append({
                **h,
                "project": proj,
                "current_price": proj["price_per_ton"],
                "current_value": round(current_value, 2),
                "invested": round(invested, 2),
                "gain": round(gain, 2),
                "gain_pct": round((gain / invested) * 100, 1) if invested else 0,
            })
            total_value += current_value
            total_invested += invested
            total_tons += h["tons_held"]
    return render_template(
        "portfolio.html",
        holdings=holdings,
        total_value=round(total_value, 2),
        total_invested=round(total_invested, 2),
        total_tons=total_tons,
        total_gain=round(total_value - total_invested, 2),
        total_gain_pct=round(((total_value - total_invested) / total_invested) * 100, 1) if total_invested else 0,
    )


@app.route("/api/prices")
def api_prices():
    return jsonify(PRICE_HISTORY)


@app.route("/api/projects")
def api_projects():
    return jsonify(PROJECTS)


@app.route("/api/transactions")
def api_transactions():
    return jsonify(TRANSACTIONS)


@app.route("/api/stats")
def api_stats():
    return jsonify(MARKET_STATS)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
