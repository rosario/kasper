#!/usr/bin/env python3

import pathlib
import sys

import filetype

from PIL import Image
from sh import convert, exiftool

def gen_gallery_item_html(file: pathlib.Path, top_dir: pathlib.Path, base_url: str):
    im = Image.open(file)
    width, height = im.size

    gallery_item_html = f"""
          <div class="grid-item">
            <a href="{base_url}/galleries/{str(file.relative_to(top_dir).parents[0])}/{file.name}" data-pswp-width="{width}" data-pswp-height="{height}" target="_blank">
              <img src="{base_url}/galleries/{str(file.relative_to(top_dir).parents[0])}/thumbnail_{file.name}" alt="" />
            </a>
          </div>
    """

    return gallery_item_html

def gen_gallery_html(gallery_dir: pathlib.Path, top_dir: pathlib.Path, base_url: str):
    gallery_items_html = ""
    for file in gallery_dir.rglob("*"):
        if not file.is_file():
            continue
        if not filetype.is_image(file):
            continue
        if file.name.startswith("thumbnail_"):
            continue

        thumbnail_file = file.parent / f"thumbnail_{file.name}"
        if not thumbnail_file.exists():
            continue

        gallery_items_html += gen_gallery_item_html(file, top_dir, base_url)

    html = f"""
    <html>
      <head>
        <link rel="stylesheet" href="{base_url}/assets/css/photoswipe/photoswipe.css">
        <script src="{base_url}/assets/js/imagesloaded/imagesloaded.pkgd.min.js"></script>
        <script src="{base_url}/assets/js/masonry/masonry.pkgd.min.js"></script>
        <style>
          .grid-item {{
            width: 210px;
            margin-bottom: 20px;
          }}
        </style>
      </head>
      <body>
        <div class="grid pswp-gallery" id="my-gallery">
          <!-- Copy and paste from here to your post -->
          {gallery_items_html}
          <!-- End copy and paste -->
        </div>
        <script type="module">
          import PhotoSwipeLightbox from "{base_url}/assets/js/photoswipe/photoswipe-lightbox.esm.min.js";
          import PhotoSwipe from "{base_url}/assets/js/photoswipe/photoswipe.esm.min.js";

          const lightbox = new PhotoSwipeLightbox({{
            gallery: "#my-gallery",
            children: "a",
            pswpModule: PhotoSwipe
          }});
          lightbox.init();
        </script>
        <script>
          var elem = document.querySelector(".grid");
          var msnry = new Masonry( elem, {{
            itemSelector: ".grid-item",
            columnWidth: 230
          }});

          imagesLoaded( elem ).on("progress", function() {{
            msnry.layout();
          }});
        </script>
      </body>
    </html>
    """

    index_file = gallery_dir / "index.html"
    with open(index_file, "w") as index_f:
        index_f.write(html)

def thumbnailify(file: pathlib.Path):
    if file.name.startswith("thumbnail"):
        return

    thumbnail_file = file.parent / f"thumbnail_{file.name}"
    if thumbnail_file.exists():
        print(f"Skipping {file}")
        return

    print(f"Thumbnailing: {file}")
    exiftool("-EXIF=", str(file))
    convert("-strip", "-thumbnail", "210x>", str(file), str(thumbnail_file))

def walk_dir(directory: pathlib.Path, base_url: str):
    gallery_dirs = set()
    for file in directory.rglob("*"):
        if not file.is_file():
            continue
        if not filetype.is_image(file):
            continue
        thumbnailify(file)
        gallery_dirs.add(file.parent)

    for gallery_dir in gallery_dirs:
        print(f"Generating gallery html for {gallery_dir}")
        gen_gallery_html(gallery_dir, directory, base_url)

def main():
    if len(sys.argv) < 2:
        print("usage: argv[0] [directory]")
        sys.exit(1)

    directory = sys.argv[1]

    if len(sys.argv) >= 2:
        base_url = sys.argv[2]
    else:
        base_url = "./"

    walk_dir(pathlib.Path(directory), base_url)

if __name__ == "__main__":
    main()
