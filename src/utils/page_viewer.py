def show_page(parsed_data, current_page, text, prev_button, next_button):
    text.clear()
    if parsed_data:
        page_data = list(parsed_data.values())[current_page]
        page_text = ""
        for key, value in page_data.items():
            page_text += f"<p><b>{key}: </b>{value}</p>"
        text.setHtml(page_text)

    prev_button.setEnabled(current_page > 0)
    next_button.setEnabled(current_page < len(parsed_data) - 1)


def prev_page(parsed_data, current_page, text, prev_button, next_button):
    current_page -= 1
    show_page(parsed_data, current_page, text, prev_button, next_button)


def next_page(parsed_data, current_page, text, prev_button, next_button):
    current_page += 1
    show_page(parsed_data, current_page, text, prev_button, next_button)
