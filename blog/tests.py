from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Blog

# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.blog = Blog.objects.create(
            title='Test blog',
            body='this is a test',
            author=self.user
        )
    
    def test_string_represantation(self):
        blog = Blog(title='A sample title')
        self.assertEqual(str(blog), blog.title)
        
    def test_content(self):
        self.assertEqual(f'{self.blog.title}', 'Test blog')
        self.assertEqual(f'{self.blog.body}', 'this is a test')
        self.assertEqual(f'{self.blog.author}', "testuser")
        
    def test_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'this is a test')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_detail_view(self):
        response = self.client.get('/blog/1/') # always iclude the /
        no_response = self.client.get('/blog/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test blog')
        self.assertTemplateUsed(response, 'blog.html')
        
    def test_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(),'/blog/1/')
        
    def test_create_view(self):
        response = self.client.post(reverse("new_blog"), {
            'title':'New title',
            'body':'New text',
            'author':self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')
        
    def test_update_view(self):
        response = self.client.post(reverse('update', args='1'),{
            'title':'updated title',
            'body':'updated body'
        })
        self.assertEqual(response.status_code, 302) #checking that it results in a redirect
        
    def test_delete_view(self):
        response = self.client.get(reverse('delete', args='1'))
        self.assertEqual(response.status_code, 200)
       
