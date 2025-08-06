import argparse
from datetime import datetime, timedelta


def format_date(d):
    """Return a date formatted as 'Weekday, DD Month YYYY'."""
    return d.strftime("%A, %d %B %Y")


def calculate_deadlines(service_date):
    """Calculate key court deadlines from the service date."""
    respond_deadline = service_date + timedelta(days=14)
    extended_deadline = service_date + timedelta(days=28)
    default_no_aos = respond_deadline + timedelta(days=1)
    default_with_aos = extended_deadline + timedelta(days=1)
    return {
        "respond_deadline": respond_deadline,
        "extended_deadline": extended_deadline,
        "default_no_aos": default_no_aos,
        "default_with_aos": default_with_aos,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Calculate court deadlines given the claim served date."
    )
    parser.add_argument(
        "service_date",
        help="Date the claim was served in YYYY-MM-DD format",
    )
    args = parser.parse_args()

    try:
        service_date = datetime.strptime(args.service_date, "%Y-%m-%d").date()
    except ValueError:
        parser.error("service_date must be in YYYY-MM-DD format")

    deadlines = calculate_deadlines(service_date)

    print(f"Claim served: {format_date(service_date)}")
    print(
        "If no Acknowledgment of Service is filed, "
        f"deadline to respond (Defence or Admission): {format_date(deadlines['respond_deadline'])}"
    )
    print(
        "If Acknowledgment of Service is filed by "
        f"{format_date(deadlines['respond_deadline'])} extended Defence deadline (28 days from service): "
        f"{format_date(deadlines['extended_deadline'])}"
    )
    print("\nDefault Judgment Eligibility")
    print(
        f"If no response is filed by {format_date(deadlines['respond_deadline'])}, "
        f"the claimant may request default judgment on or after {format_date(deadlines['default_no_aos'])}."
    )
    print(
        "If Acknowledgment was filed, default judgment may be requested on or after "
        f"{format_date(deadlines['default_with_aos'])}, if no Defence was filed."
    )


if __name__ == "__main__":
    main()
