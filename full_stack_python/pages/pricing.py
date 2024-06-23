import reflex as rx
from ..ui.base import base_page


def pricing_page() -> rx.Component:
    # Welcome Page (Index)
        
    my_child = rx.vstack(
        rx.heading("Our Prices", size="9"),
        rx.text(
            "This is the price page "
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center",
        text_align="center",
        id="my_child",
    )
    return base_page(my_child)