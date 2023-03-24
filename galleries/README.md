# galleries

Enable photo galleries in your posts!

## How

1) Set up the gallery directories

Create subdirectories per gallery and put images per directory.

eg.
```
.
├── gallery-1
│   ├── alex-quezada-UsVoHGRjWAs-unsplash.jpg
│   ├── andrew-castillo-jkK8B9brrS4-unsplash.jpg
│   ├── clark-van-der-beken-l2AmhAw8hyk-unsplash.jpg
├── gallery-2
│   ├── kristaps-ungurs-8sehVODwNtk-unsplash.jpg
│   ├── louis-de-jarzat-00YHwl4xVsM-unsplash.jpg
│   ├── madita-luisa-sUoTw-E13ww-unsplash.jpg
```

2) Run thumbnail.sh

Execute thumbnail.sh to generate thumbnail files for the images in the
galleries and index.html files. Modify thumbnail.sh to change the base_url
variable if you wish to fix the url prefixes in the index.html.

```
./thumbnail.sh
```

3) Copy and paste html

The index.html files per gallery directory contains the html for the post
gallery. Find the html comments indicating the copy and paste sections and
copy into your posts.

4) Replace base url in gallery html

Replace the url prefix with "{{ site.baseurl }}".

eg. `http://127.0.0.1:4000/dark-kasper => {{ site.baseurl }}`

5) Add galleries variable

At the top of your post, set the galleries variable (a list of gallery ids
is expected). The galleries should have ids like: "gallery-one" or "gallery-x".
The expected galleries variable would then be:

```
galleries:
  - one
  - x
```
