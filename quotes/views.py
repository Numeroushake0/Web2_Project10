from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Quote, Author, Tag
from .forms import QuoteForm, AuthorForm

class QuoteListView(ListView):
    model = Quote
    template_name = 'quotes/quote_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_tags'] = Tag.objects.all()[:10]  # топ-10 тегів
        return context

class QuoteDetailView(DetailView):
    model = Quote
    template_name = 'quotes/quote_detail.html'

class AddAuthorView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'quotes/add_author.html'
    success_url = '/'

class AddQuoteView(LoginRequiredMixin, CreateView):
    model = Quote
    form_class = QuoteForm
    template_name = 'quotes/add_quote.html'
    success_url = '/'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'quotes/signup.html'
    success_url = '/login/'

class QuotesByTagView(ListView):
    model = Quote
    template_name = 'quotes/quote_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Quote.objects.filter(tags__name=self.kwargs['tag_name'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_tags'] = Tag.objects.all()[:10]
        return context
