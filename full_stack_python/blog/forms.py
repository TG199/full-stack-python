import reflex as rx

from ..ui.base import base_page
from ..import contact
from .. import navigation
from .state import (
    BlogAddPostFormState,
    BlogEditFormState
)

        
def blog_post_add_form() -> rx.Component:
    # Welcome Page (Index)
    return rx.form(
            rx.vstack(
                rx.hstack(
                    
                    rx.input(
                        name="title",
                        placeholder="Title",
                        Required=True,
                        width='100%'
                    ),
                    width='100%'
                ),
                rx.text_area(
                    name='content',
                    placeholder='Your message',
                    required=True,
                    height='50vh',
                    width='100%',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=BlogAddPostFormState.handle_submit,
            reset_on_submit=True,
    )
    
    
def blog_post_edit_form() -> rx.Component:
    # Welcome Page (Index)
    post = BlogEditFormState.post
    title = post.title
    post_content = BlogEditFormState.post_content
    return rx.form(
            rx.box(
              
                rx.input(
                    type='hidden',
                    name='post_id',
                    value=post.id
                ),
                display='none'
            ),
            rx.vstack(
                rx.hstack(
                    
                    rx.input(
                        default_value=title,
                        name="title",
                        placeholder="Title",
                        Required=True,
                        width='100%'
                    ),
                    width='100%'
                ),
                rx.text_area(
                    value = post_content,
                    on_change = BlogEditFormState.set_post_content,
                    name='content',
                    placeholder='Your message',
                    required=True,
                    height='50vh',
                    width='100%',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=BlogEditFormState.handle_submit,
    )
    