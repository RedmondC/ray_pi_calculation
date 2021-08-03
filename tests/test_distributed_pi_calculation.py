import unittest
from src.monte_carlo_pi_calculation import monte_carlo_pi_estimation


class DistributedPiCalculationTest(unittest.TestCase):
    def test_calc_pi(self):
        """
        Tests to verify monte_carlo_pi_estimation method.
        :return: Pass or Fail
        """
        answer = monte_carlo_pi_estimation(9000000)
        self.assertEqual(3.14, float(f"{answer:.{2}f}"))

        answer = monte_carlo_pi_estimation(70000000)
        self.assertAlmostEqual(3.1415, float(f"{answer:.{4}f}"), places=5)

        answer = monte_carlo_pi_estimation(-1)
        self.assertEqual(0.00, float(f"{answer:.{2}f}"))


if __name__ == "__main__":
    unittest.main()
