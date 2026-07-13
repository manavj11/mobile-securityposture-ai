"""
CLI entry point.
"""

from pprint import pprint

from detector import DeviceDetector
from mock_devices import get_device


def main():

    detector = DeviceDetector()

    profile = "rooted"

    device = get_device(profile)

    result = detector.analyze(device)

    print("=" * 60)
    print(f"Mock Device: {profile}")
    print("=" * 60)

    pprint(device)

    print("\nAnalysis")
    print("-" * 60)

    print(f"Anomaly Score : {result['score']}")
    print(f"Risk Level    : {result['risk']}")
    print(f"LLM Allowed   : {result['allow_llm']}")


if __name__ == "__main__":
    main()