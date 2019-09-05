/*
 * This is a JavaScript Scratchpad.
 *
 * Enter some JavaScript, then Right Click or choose from the Execute Menu:
 * 1. Run to evaluate the selected text (Ctrl+R),
 * 2. Inspect to bring up an Object Inspector on the result (Ctrl+I), or,
 * 3. Display to insert the result in a comment after the selection. (Ctrl+L)
 */

{
  
const languages = ["clojure", "javascript", "python", "scheme", "ruby"]
const langToSelectorName = {
  clojure: 'selector',
  javascript: 'selector_eval_js',
  python: 'selector_eval_python_client',
  scheme: 'selector_eval_scheme',
  ruby: 'selector_eval_ruby',
};
  
  

let jsSrc = (lang) => {
    if (lang === 'clojure') {
        return 'https://storage.googleapis.com/app.klipse.tech/plugin/js/klipse_plugin.js'
    }
    return 'https://storage.googleapis.com/app.klipse.tech/plugin_prod/js/klipse_plugin.min.js'
}


let createIFrame = (lang,src) => {
    let selectorName = langToSelectorName[lang];
    return `<iframe height="500px" width="100%" srcdoc='
    <pre><code class=&quot;klipse&quot;>${src}</code></pre>

      <link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;https://storage.googleapis.com/app.klipse.tech/css/codemirror.css&quot;>

      <script>
        window.klipse_settings = {
        ${selectorName}: &quot;.klipse&quot;
        };
      </script>
      <script src=&quot;${jsSrc(lang)}&quot;></script>
    '>
    </iframe>`
};

    let klipsify = (elem) => {
        let classes = elem.className;
        let lang = "";
        for (l of languages) {
          if (classes.includes(l)) {
            lang = l;
          }
        }
        console.log(lang)
        if (l) {
          elem.parentNode.innerHTML = createIFrame(lang, elem.innerHTML);
        }
        return elem;
    }

    document.querySelectorAll('code').forEach(x => klipsify(x))
}

/*
Exception: SyntaxError: missing variable name
@Scratchpad/1:51
*/
/*
Exception: SyntaxError: missing ) after argument list
@Scratchpad/1:55
*/