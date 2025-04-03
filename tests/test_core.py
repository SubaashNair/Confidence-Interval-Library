import pytest
import numpy as np
from stats_confidence_intervals.core import (
    mean_confidence_interval,
    proportion_confidence_interval,
    ConfidenceInterval,
    validate_confidence_level,
    validate_data
)

class TestConfidenceIntervals(unittest.TestCase):
    def test_validate_confidence_level(self):
        """Test confidence level validation."""
        with self.assertRaises(ValueError):
            validate_confidence_level(0)
        with self.assertRaises(ValueError):
            validate_confidence_level(1)
        with self.assertRaises(ValueError):
            validate_confidence_level(-0.5)
        with self.assertRaises(ValueError):
            validate_confidence_level(1.5)
        # This should not raise an error
        validate_confidence_level(0.95)

    def test_validate_data(self):
        """Test data validation."""
        with self.assertRaises(ValueError):
            validate_data([])
        with self.assertRaises(ValueError):
            validate_data(['a', 'b', 'c'])
        # These should not raise errors
        validate_data([1, 2, 3])
        validate_data([1.5, 2.5, 3.5])

    def test_mean_confidence_interval(self):
        """Test mean confidence interval calculation."""
        data = [1, 2, 3, 4, 5]
        ci = mean_confidence_interval(data)
        
        self.assertIsInstance(ci, ConfidenceInterval)
        self.assertAlmostEqual(ci.estimate, 3.0)
        self.assertLess(ci.lower_bound, ci.estimate)
        self.assertGreater(ci.upper_bound, ci.estimate)
        self.assertEqual(ci.confidence_level, 0.95)

        # Test with different confidence level
        ci_90 = mean_confidence_interval(data, confidence=0.90)
        self.assertEqual(ci_90.confidence_level, 0.90)
        # 90% CI should be narrower than 95% CI
        self.assertGreater(ci_90.lower_bound, ci.lower_bound)
        self.assertLess(ci_90.upper_bound, ci.upper_bound)

    def test_proportion_confidence_interval(self):
        """Test proportion confidence interval calculation."""
        # Test with Wilson method
        ci_wilson = proportion_confidence_interval(7, 10, method='wilson')
        self.assertIsInstance(ci_wilson, ConfidenceInterval)
        self.assertAlmostEqual(ci_wilson.estimate, 0.7)
        self.assertLess(ci_wilson.lower_bound, ci_wilson.estimate)
        self.assertGreater(ci_wilson.upper_bound, ci_wilson.estimate)

        # Test with normal approximation method
        ci_normal = proportion_confidence_interval(7, 10, method='normal')
        self.assertIsInstance(ci_normal, ConfidenceInterval)
        self.assertAlmostEqual(ci_normal.estimate, 0.7)

        # Test invalid inputs
        with self.assertRaises(ValueError):
            proportion_confidence_interval(11, 10)  # successes > total
        with self.assertRaises(ValueError):
            proportion_confidence_interval(5, 0)    # total <= 0
        with self.assertRaises(ValueError):
            proportion_confidence_interval(5, 10, method='invalid')  # invalid method

if __name__ == '__main__':
    unittest.main()
