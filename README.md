### Hexlet tests and linter status:
[![Actions Status](https://github.com/SvamiBog/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/SvamiBog/python-project-50/actions)
[![Github Actions Status](https://github.com/SvamiBog/python-project-50/workflows/Python%20CI/badge.svg)](https://github.com/SvamiBog/python-project-50/actions)

<a href="https://codeclimate.com/github/SvamiBog/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/15004deb7affd813108a/maintainability" /></a>
<a href="https://codeclimate.com/github/SvamiBog/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/15004deb7affd813108a/test_coverage" /></a>


<body>
    <h1>Вычислитель отличий</h1>
    <p>Проект "Вычислитель отличий" является учебным проектом на курсе "Python-разработчик" на платформе Хекслет. Это инструмент командной строки, который помогает определить разницу между двумя структурами данных.</p>
    <h2>Функциональность</h2>
    <ul>
        <li>Поддержка форматов JSON и YAML.</li>
        <li>Вывод различий в формате plain text, структурированного текста или JSON.</li>
        <li>Работа с файлами и данными из командной строки.</li>
    </ul>
    <h2>Установка</h2>
    <p>Для работы с "Вычислителем отличий" убедитесь, что у вас установлен Python версии 3.6 или выше.</p>
    <ol>
        <li>Клонировать репозиторий:
            <pre><code>git clone https://github.com/your-github-account/difference-calculator.git</code></pre>
        </li>
        <li>Перейти в каталог проекта:
            <pre><code>cd difference-calculator</code></pre>
        </li>
        <li>Установить зависимости:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>
    <h2>Примеры использования</h2>
    <h3>Сравнение плоских файлов (JSON):</h3>
    <pre><code>gendiff filepath1.json filepath2.json</code></pre>
  <a href="https://asciinema.org/a/pUQAAhi1VPnCAXGwA60WqJ6Lc" target="_blank"><img src="https://asciinema.org/a/pUQAAhi1VPnCAXGwA60WqJ6Lc.svg" /></a>
    <h3>Сравнение файлов с выводом в структурированном виде:</h3>
    <pre><code>gendiff --format stylish filepath1.yaml filepath2.yaml</code></pre>
  <a href="https://asciinema.org/a/DQCRcppGLI2dHPGXyRHdoIfCu" target="_blank"><img src="https://asciinema.org/a/DQCRcppGLI2dHPGXyRHdoIfCu.svg" /></a>
    <h3>Сравнение файлов с выводом в plain:</h3>
    <pre><code>gendiff --format plain filepath1.json filepath2.json</code></pre>
  <a href="https://asciinema.org/a/5dqzrOZdor8NYCBSTXniYXyYQ" target="_blank"><img src="https://asciinema.org/a/5dqzrOZdor8NYCBSTXniYXyYQ.svg" /></a>
    <h3>Сравнение файлов с выводом в JSON:</h3>
    <pre><code>gendiff --format json filepath1.yaml filepath2.yaml</code></pre>
  <a href="https://asciinema.org/a/mklimjcNQb42Ok3SXJoPYXLDB" target="_blank"><img src="https://asciinema.org/a/mklimjcNQb42Ok3SXJoPYXLDB.svg" /></a>
</body>


