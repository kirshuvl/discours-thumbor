Thumbor Filter for Discours
===

This plugins provide a way to generate text via Thumbor Filter.
## Quick Start
```
docker build -t thumbor_discours .
docker run -d -p 80:80 thumbor_discours
```
## Local Development
```
python -m venv venv
pip install pillow
python discours-text-filter/discours_text/filter.py
```
Last command is returning new image after default `discourstext` filter and save it with output.webp name
## Usage
Add `discourstext()` to thumbor url at `filters` section, method signature is like this: 

`discourstext(category, author, title)`

Here'are some examples:

```
http://thumbor/unsafe/filters:discourstext('общество','Иван Иванов','Заголовок статьи')/your-image-url
http://thumbor/unsafe/filters:discourstext('проза','Игорь Игоревич','Быть? Или не быть?')/your-image-url
```
## Full url example

http://localhost/unsafe/filters:discourstext('%D0%9E%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%BE','%D0%9F%D0%BE%D0%BB%D0%B8%D0%BD%D0%B0%20%D0%94%D1%83%D0%B3%D0%B0%D0%BD%D0%BE%D0%B2%D0%B0','%C2%AB%D0%9C%D0%BE%D0%B9%20%D1%80%D0%B5%D0%B1%D0%B5%D0%BD%D0%BE%D0%BA%20%D1%81%D0%B8%D0%B4%D0%B8%D1%82%20%D0%B7%D0%B0%20%D0%BD%D0%B5%D1%81%D0%BE%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%BF%D1%80%D0%B5%D1%81%D1%82%D1%83%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%C2%BB.%20%D0%9C%D0%B0%D0%BC%D0%B0%20%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%BE%D0%B4%D1%80%D0%BE%D1%81%D1%82%D0%BA%D0%B0%20%D0%9D%D0%B8%D0%BA%D0%B8%D1%82%D1%8B%20%D0%A3%D0%B2%D0%B0%D1%80%D0%BE%D0%B2%D0%B0%20%D0%BE%20%D0%BF%D1%80%D0%B8%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D0%B5%20%D0%B8%20%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D0%B0%D1%85%20%D1%81%D1%8B%D0%BD%D0%B0')/https://assets.discours.io/unsafe/1600x/production/image/541938e0-9995-11ee-af78-1b150ab75706.JPG

---

## Copyright

MIT