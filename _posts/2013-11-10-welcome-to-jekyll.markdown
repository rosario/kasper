---
layout: post
title:  "Welcome to Jekyll!"
date:   2013-11-10 10:18:00
categories: Thriller Comedy Horror
galleries:
  - one
  - two
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

And here is an image gallery of random unsplash images displayed using photoswipe, masonry
and imagesloaded. See /galleries for details on how to set up your own galleries.

<div class="grid pswp-gallery" id="gallery-one">
  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-1/louis-de-jarzat-00YHwl4xVsM-unsplash.jpg" data-pswp-width="4000" data-pswp-height="2250" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-1/thumbnail_louis-de-jarzat-00YHwl4xVsM-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-1/clark-van-der-beken-l2AmhAw8hyk-unsplash.jpg" data-pswp-width="2861" data-pswp-height="4444" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-1/thumbnail_clark-van-der-beken-l2AmhAw8hyk-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-1/mary-brennan-3AdpK0ib5ko-unsplash.jpg" data-pswp-width="4661" data-pswp-height="6991" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-1/thumbnail_mary-brennan-3AdpK0ib5ko-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-1/alex-quezada-UsVoHGRjWAs-unsplash.jpg" data-pswp-width="4085" data-pswp-height="6128" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-1/thumbnail_alex-quezada-UsVoHGRjWAs-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-1/kristaps-ungurs-8sehVODwNtk-unsplash.jpg" data-pswp-width="5985" data-pswp-height="3982" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-1/thumbnail_kristaps-ungurs-8sehVODwNtk-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-1/patryk-wojcieszak-MN0mhf9kr_o-unsplash.jpg" data-pswp-width="2133" data-pswp-height="3200" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-1/thumbnail_patryk-wojcieszak-MN0mhf9kr_o-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-1/madita-luisa-sUoTw-E13ww-unsplash.jpg" data-pswp-width="4000" data-pswp-height="5600" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-1/thumbnail_madita-luisa-sUoTw-E13ww-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-1/masahiro-miyagi-EesGu5cRnWo-unsplash.jpg" data-pswp-width="5208" data-pswp-height="3583" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-1/thumbnail_masahiro-miyagi-EesGu5cRnWo-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-1/andrew-castillo-jkK8B9brrS4-unsplash.jpg" data-pswp-width="3265" data-pswp-height="4898" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-1/thumbnail_andrew-castillo-jkK8B9brrS4-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-1/karl-paul-baldacchino-0Eup9Wiit7E-unsplash.jpg" data-pswp-width="4000" data-pswp-height="6000" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-1/thumbnail_karl-paul-baldacchino-0Eup9Wiit7E-unsplash.jpg" alt="" />
    </a>
  </div>

</div>

And here is another photo gallery.

<div class="grid pswp-gallery" id="gallery-two">
  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-2/leon-rohrwild-XqJyl5FD_90-unsplash.jpg" data-pswp-width="6240" data-pswp-height="4160" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-2/thumbnail_leon-rohrwild-XqJyl5FD_90-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-2/luis-magallon-rK4p0vUjVKc-unsplash.jpg" data-pswp-width="8000" data-pswp-height="6000" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-2/thumbnail_luis-magallon-rK4p0vUjVKc-unsplash.jpg" alt="" />
    </a>
  </div>

  <div class="grid-item">
    <a href="{{ site.baseurl }}/galleries/gallery-2/simon-0EkEV2fKVCs-unsplash.jpg" data-pswp-width="4160" data-pswp-height="6240" target="_blank">
      <img src="{{ site.baseurl }}/galleries/gallery-2/thumbnail_simon-0EkEV2fKVCs-unsplash.jpg" alt="" />
    </a>
  </div>
</div>

Here are some tags to show the styling:

&lt;kbd&gt;: <kbd>Helloworld!</kbd>

Check out the [Jekyll docs][jekyll] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll's GitHub repo][jekyll-gh].

[jekyll-gh]: https://github.com/mojombo/jekyll
[jekyll]:    http://jekyllrb.com
