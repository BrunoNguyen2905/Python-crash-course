import json
from typing import Any, Protocol


class Exporter(Protocol):
    def export(self, data: dict[str, Any]) -> str:
        ...


class JSONExporter:
    def export(self, data: dict[str, Any]) -> str:
        import json
        return json.dumps(data, indent=2)


class CSVExporter:
    def export(self, data: dict[str, Any]) -> str:
        return ",".join(f"{key}={value}" for key, value in data.items())


# def generate_report(data: dict[str, Any], exporter: JSONExporter | CSVExporter) -> str:
def generate_report(data: dict[str, Any], exporter: Exporter) -> str:
    return exporter.export(data)


def main() -> None:
    data = {"sales": 1000, "customers": 150, "region": "North"}

    json_exporter = JSONExporter()
    csv_exporter = CSVExporter()

    json_report = generate_report(data, json_exporter)
    csv_report = generate_report(data, csv_exporter)

    print("JSON Report:")
    print(json_report)
    print("\nCSV Report:")
    print(csv_report)


if __name__ == "__main__":
    main()


# Inputs should be as wide as possible (e.g., using Protocols or base classes), as generic as possible (e.g., using Generics), contravariant where possible (e.g., function parameters), and covariant where needed (e.g., return types).
# Outputs should be as specific as possible (e.g., using concrete classes) and covariant where possible (e.g., return types).
