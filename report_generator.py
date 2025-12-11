import os

class ReportGenerator:
    def __init__(self, output_path):
        self.output_path = output_path
        self.content = []

    def add_header(self, title, level=1):
        self.content.append(f"{'#' * level} {title}\n")

    def add_text(self, text):
        self.content.append(f"{text}\n")

    def add_metrics_table(self, metrics_dict, title="Model Metrics"):
        self.add_header(title, level=3)
        self.content.append("| Metric | Value |")
        self.content.append("|---|---|")
        for key, value in metrics_dict.items():
            if isinstance(value, float):
                self.content.append(f"| {key} | {value:.4f} |")
            else:
                self.content.append(f"| {key} | {value} |")
        self.content.append("\n")

    def add_image(self, image_path, caption):
        rel_path = os.path.relpath(image_path, os.path.dirname(self.output_path))
        self.content.append(f"![{caption}]({rel_path})\n")

    def save(self):
        with open(self.output_path, 'w') as f:
            f.write("\n".join(self.content))
