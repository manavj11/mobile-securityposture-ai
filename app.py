"""
CLI entry point.
"""

from pprint import pprint

from detector import DeviceDetector
from llm import get_recommendation
from mock_devices import get_device


def main():

    detector = DeviceDetector()

    profile = "developer"

    device = get_device(profile)

    result = detector.analyze(device)

    print("=" * 60)
    print(f"Mock Device: {profile}")
    print("=" * 60)

    pprint(device)

    print("\nAnalysis")
    print("-" * 60)

    print(f"Score        : {result['score']}")
    print(f"Risk         : {result['risk']}")

    if result["allow_llm"]:

        print("\nRecommendations")
        print("-" * 60)

        try:
            recommendation = get_recommendation(
                device=device,
                risk=result["risk"],
            )
            print(recommendation)

        except Exception as e:
            print(f"LLM unavailable: {e}")

    else:

        print("\nRecommendations")
        print("-" * 60)
        print("Manual review required.")


if __name__ == "__main__":
    main()