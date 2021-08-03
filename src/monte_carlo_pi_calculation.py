import random
import ray
import logging
from datetime import datetime
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__, template_folder="templates")
num_workers = 8


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    """
    Starts ray pi value estimation while logging the time taken to run calculation.
    :param request: Contains arguments
        - precision (n)
        - iterations (x)
    :return: Pi value estimation to "precision" decimal places.
    """
    precision = int(request.args.get("precision", None))
    iterations = int(request.args.get("iterations", None))
    logging.info("Starting calculation!")
    start_time = datetime.now()
    results = ray.get(
        [ray_calc_pi.remote(iterations // num_workers) for x in range(num_workers)]
    )
    pi = 0
    for result in results:
        pi += result
    logging.info(f"Time taken :{datetime.now() - start_time}!")
    return f"{(pi / num_workers):.{precision}f}"


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Homepage which allows for posting of input values for calculation initialisation.
    :param request: Contains arguments
        - precision (n)
        - iterations (x)
    :return: Homepage or redirects to calculation page.
    """
    if request.method == "POST":
        precision = request.form["n"]
        iterations = request.form["x"]
        return redirect(
            url_for("calculate", precision=precision, iterations=iterations)
        )
    return render_template("index.html")


def monte_carlo_pi_estimation(iterations: int) -> float:
    """
    Calculates an estimation of pi using the mote carlo method using "iterations" number of points.
    :param iterations: Number of points to generate.
    :return: Estimation of pi.
    """
    logging.info("worker created!")
    internal_points = 0
    total_points = 0

    for i in range(iterations):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
        origin_dist = rand_x ** 2 + rand_y ** 2

        if origin_dist <= 1:
            internal_points += 1
        total_points += 1

    if total_points > 0:
        pi = 4 * internal_points / total_points
    else:
        pi = 0
    return pi


if __name__ == "__main__":
    ray.init()

    ray_calc_pi = ray.remote(monte_carlo_pi_estimation)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    app.run()
