"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from .ui.base import base_page
from . import blog, contact, navigation, pages

class State(rx.State):
    """The app state."""
    
    label: str = "Goal Ball!"
    
    def handle_title_input_change(self, val):
        self.label = val
    ...

def index() -> rx.Component:
    # Welcome Page (Index)
        
    my_child = rx.vstack(
        rx.heading(State.label, size="9"),
        rx.text(
            "Get started by editing ",
            rx.code(f"{config.app_name}/{config.app_name}.py"),
            size="5",
        ),
        rx.link(
            rx.button("About us"),
            href=navigation.routes.PRICING_ROUTE,
        ),
        spacing="5",
        justify="center",
        min_height="85vh",
        align="center",
        text_align="center",
        id="my_child",
    )
    return base_page(my_child)

app = rx.App()
app.add_page(index)
app.add_page(pages.about_page,
             route=navigation.routes.ABOUT_ROUTE)
app.add_page(contact.contact_page,
             route=navigation.routes.CONTACT_ROUTE)

#blogpage
app.add_page(blog.blog_post_list_page,
             route=navigation.routes.BLOG_POSTS_ROUTE,
             on_load=blog.BlogPostState.load_posts)

app.add_page(
    blog.blog_post_add_page,
    route=navigation.routes.BLOG_POST_ADD_ROUTE
    )


app.add_page(
             blog.blog_post_detail_page,
             route="/blog/[blog_id]",
             on_load=blog.BlogPostState.get_post_detail
             )
app.add_page(
             blog.blog_post_detail_page,
             route="/blog/[blog_id]/edit",
             on_load=blog.BlogPostState.get_post_detail
             )

app.add_page(contact.contact_entries_list_page,
             route=navigation.routes.CONTACT_ENTRIES_ROUTE,
             on_load=contact.ContactState.list_entries)
app.add_page(pages.pricing_page,
             route=navigation.routes.PRICING_ROUTE)

