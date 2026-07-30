from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def generate_dashboard_report(metrics, insights):
    """
    Generate a PDF dashboard report.
    Returns the PDF as a BytesIO object.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    # ==========================
    # Title
    # ==========================

    elements.append(
        Paragraph("<b>MetricMind Dashboard Report</b>", styles["Title"])
    )

    elements.append(
        Paragraph("AI Powered Business Intelligence Platform", styles["Heading2"])
    )

    elements.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # ==========================
    # KPI Summary
    # ==========================

    elements.append(
        Paragraph("<b>Key Performance Indicators</b>", styles["Heading2"])
    )

    for key, value in metrics.items():
        elements.append(
            Paragraph(f"{key}: {value}", styles["BodyText"])
        )

    elements.append(
        Paragraph("<br/>", styles["Normal"])
    )

    # ==========================
    # AI Insights
    # ==========================

    elements.append(
        Paragraph("<b>AI Business Insights</b>", styles["Heading2"])
    )

    for item in insights:

        elements.append(
            Paragraph(
                f"{item['icon']} <b>{item['title']}</b>",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                item["message"],
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                "<i>" + item["recommendation"] + "</i>",
                styles["Italic"],
            )
        )

        elements.append(
            Paragraph("<br/>", styles["Normal"])
        )

    doc.build(elements)

    buffer.seek(0)

    return buffer