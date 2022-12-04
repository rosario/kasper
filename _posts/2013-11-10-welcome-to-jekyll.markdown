---
layout: post
title:  "Welcome to Jekyll!"
date:   2013-11-10 10:18:00
categories: Thriller Comedy Horror
---

You'll find this post in your `_posts` directory - edit this post and re-build (or run with the `-w` switch) to see your changes!
To add new posts, simply add a file in the `_posts` directory that follows the convention: YYYY-MM-DD-name-of-post.ext.

Jekyll also offers powerful support for code snippets:

{% highlight python %}
# A comment
class Person:
  """A class"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

# A comment
# Another comment
# Yet another comment

print(p1.name)
print(p1.age)
{% endhighlight %}

Yet another:

{% highlight bash %}
$ echo "Helloworld"
Helloworld
{% endhighlight %}

And here is a table:

| Priority apples | Second priority | Third priority |
|-------|--------|---------|
| ambrosia | gala | red delicious |
| pink lady | jazz | macintosh |
| honeycrisp | granny smith | fuji |

And here is an image:

![image description]({{ site.baseurl }}/assets/images/example-image.png)

Here are some tags to show the styling:

&lt;kbd&gt;: <kbd>Helloworld!</kbd>

Check out the [Jekyll docs][jekyll] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll's GitHub repo][jekyll-gh].

[jekyll-gh]: https://github.com/mojombo/jekyll
[jekyll]:    http://jekyllrb.com
