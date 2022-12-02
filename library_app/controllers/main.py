from odoo import http

class Books(http.Controller):

    @http.route("/library/books")
    def list(self, **kwargs):
        Book = http.request.env["product.template"]
        books = Book.search([])
        return http.request.render(
            "library_app.book_list_template",
            {"books": books}
        )
