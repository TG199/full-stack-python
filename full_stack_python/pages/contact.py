import reflex as rx
import asyncio

from ..ui.base import base_page
from .. import navigation

class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    timeleft: int = 5
    
    @rx.var
    def timeleft_label(self):
        if self.timeleft < 0:
            return "No time left"
        return f"{self.timeleft} seconds!"
    @rx.var
    def thank_you(self):
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}".strip() + "!"
    
    async def handle_submit(self, form_data: dict):
        """Handle the form data"""
        self.form_data = form_data
        self.did_submit = True
        yield
        await asyncio.sleep(2)
        self.did_submit = False
        
    async def start_timer(self):
        while self.timeleft > 0:
            await asyncio.sleep(1)
            self.timeleft -= 1
            yield
        
@rx.page(
    on_load=ContactState.start_timer,
    route=navigation.routes.CONTACT_ROUTE
)
def contact_page() -> rx.Component:
    # Welcome Page (Index)
    my_form = rx.form(
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
            
    my_child = rx.vstack(
        rx.heading("Contact Us", size="9"),
        rx.text(ContactState.timeleft),
        rx.cond(ContactState.did_submit, 
                ContactState.thank_you, ""), 
        rx.desktop_only(
            rx.box(
                my_form,
                width='50vw'
            )
        ),
         rx.tablet_only(
            rx.box(
                my_form,
                width='75vw'
            )
        ),
        rx.mobile_only(
            rx.box(
                my_form,
                width='77vw'
            )
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center",
        text_align="center",
        id="my_child",
    )
    return base_page(my_child)