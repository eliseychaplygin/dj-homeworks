from django.views import generic
from books.models import Book


class BookListView(generic.ListView):

    model = Book
    context_object_name = 'books_list'
    template_name = 'books/books_list.html'

    def get_queryset(self):
        if self.kwargs:
            queryset = Book.objects.filter(pub_date=self.kwargs['pub_date'])
            return queryset
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs:
            date = self.kwargs['pub_date']
            context['pub_date'] = date
            previous_object = Book.objects.order_by('pub_date').filter(pub_date__lt=date).last()
            if previous_object:
                previous_date = str(previous_object.pub_date)
                context['previous_date'] = previous_date
            next_object = Book.objects.order_by('pub_date').filter(pub_date__gt=date).first()
            if next_object:
                next_date = str(next_object.pub_date)
                context['next_date'] = next_date
        return context

