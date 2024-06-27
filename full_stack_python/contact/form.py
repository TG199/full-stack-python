import reflex as rx

from ..ui.base import base_page
from ..import contact
from .. import navigation
from .state import ContactState

        
def contact_form() -> rx.Component:
    # Welcome Page (Index)
    return rx.form(
            rx.vstack(
                rx.hstack(
                    
                    rx.input(
                        name="first_name",
                        placeholder="First Name",
                        Required=True,
                        width='100%'
                    ),
                    rx.input(
                        name="last_name",
                        placeholder="Last Name",
                        width='100%'
                    ),
                    width='100%'
                ),
                rx.input(
                    name='email',
                    type='email',
                    placeholder='Your email',
                    width='100%'

                ),
                rx.text_area(
                    name='message',
                    placeholder='Your message',
                    width='100%'
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
            jusify="center"
    )           