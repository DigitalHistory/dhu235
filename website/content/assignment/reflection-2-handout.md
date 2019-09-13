---
title: "Reflection 02: Handout and Preliminary Exercises"
author: ["Matt Price"]
lastmod: 2019-09-12T09:55:43-04:00
tags: ["assignment"]
draft: false
banner: "testbanner"
menu:
  main:
    weight: 1004
    identifier: "reflection-02-handout-and-preliminary-exercises"
    parent: "Assignments"
---

In this assignment, you will **encode** parts of a thousand-year-old poem using a markup language, **display** the marked-up text in a web browser using a computational translator, and **discuss** this exercise using the idea of **deformance** as a guide.  This handout **should** contain everything you need to complete the assignment, but please use the discussion forum to ask any technical (or other!) questions.


## The Poem: “The Ruin” (from the tenth century Exeter Book), translated by Sian Echard, silently emended {#the-poem-the-ruin-from-the-tenth-century-exeter-book-translated-by-sian-echard-silently-emended}

"[The Ruin](http://faculty.arts.ubc.ca/sechard/oeruin.htm)" was likely written in the 8th or 9th century, and recorded in the [Exeter Book](https://en.wikipedia.org/wiki/Exeter%5FBook) in the 10th century. The only surviving copy has a large burn down the centre of the page that renders parts of the poem illegible. (See [this blog post](https://sites.nd.edu/manuscript-studies/2017/11/20/ivory-in-the-rust-reading-the-old-english-ruin-in-south-bend) for a substantive discussion of the poem.)

{{< figure src="https://sites.nd.edu/manuscript-studies/files/2017/11/Fahey-Screen-Shot-2017-11-17-at-6.13.25-PM-768x585.png" caption="Figure 1: _Exeter Cathedral Library MS 3501, f. 124r, all rights reserved Dean & Chapter Exeter Cathedral_" >}}


### Transcription {#transcription}

1.  Wondrous is this wall-stead, wasted by fate.
2.  Battlements broken, giant's work shattered.
3.  Roofs are in ruin, towers destroyed,
4.  Broken the barred gate, rime on the plaster,
5.  walls gape, torn up, destroyed,
6.  consumed by age. Earth-grip holds
7.  the proud builders, departed, long lost,
8.  and the hard grasp of the grave, until a hundred generations
9.  of people have passed. Often this wall outlasted,
10. hoary with lichen, red-stained, withstanding the storm,
11. one reign after another; the high arch has now fallen.
12. The wall-stone still stands, hacked by weapons,
13. by grim-ground files.
14. ...
15. ...
16. ...
17. ...
18. Mind quickened ... and the artificer,
19. skilled in round-building, bound the wall-base,
20. wondrously with iron.
21. Bright were the halls, many the baths,
22. High the gables, great the joyful noise,
23. many the mead-hall full of pleasures.
24. Until fate the mighty overturned it all.
25. Slaughter spread wide, pestilence arose,
26. and death took all those brave men away.
27. Their bulwarks were broken, their halls laid waste,
28. the cities crumbled, those who would repair it
29. laid in the earth. And so these halls are empty,
30. and the curved arch sheds its tiles,
31. torn from the roof. Decay has brought it down,
32. broken it to rubble. Where once many a warrior,
33. high of heart, gold-bright, gleaming in splendour,
34. proud and wine-flushed, shone in armour,
35. looked on a treasure of silver, on precious gems,
36. on riches of pearl...
37. in that bright city of broad rule.
38. Stone courts once stood there, and hot streams gushed forth,
39. wide floods of water, surrounded by a wall,
40. in its bright bosom, there where the baths were,
41. hot in the middle.
42. Hot streams ran over hoary stone
43. into the ringed water where baths were
44. ...
45. ...
46. That was a noble thing, the house and the city.


## Deformance {#deformance}

We will discuss in class this [portmanteau](https://en.wikipedia.org/wiki/Portmanteau) term coined by Lisa Samuels and Jerome McGann, a combination of “deform” and “performance.” Be sure you have some grasp of what this means!


## Introduction to XML,XSLT, TEI, and HTML (!) {#introduction-to-tei}

[TEI](https://cdrh.unl.edu/articles/basicguide/TEI) is a [markup language](https://en.wikipedia.org/wiki/Markup%5Flanguage) -- a system for annotating documents that can be read an processed by other compute programs.  It is a format, or defined feature set, of the [XML](https://www.w3schools.com/xml/xml%5Fwhatis.asp) "metalanguage", a very widely-used system for structuring and processing many kinds of data.  Digital humanists use TEI to turn literary texts into structured data that can be manipulated and queried in many ways, but especially on the web.

The process of turning a TEI document into a visual representation on a screen is complex:

-   first, the text must be **marked up** -- textual elements must be identified and annotated (we'll discuss how this works in more detail very soon).  This work can be both painstaking and tedious
-   next, a **translation scheme must be written** that _processes_ the xml text into [HTML](https://en.wikipedia.org/wiki/HTML), the main language of the web. This translation is almost always written in a language called [XLST](https://en.wikipedia.org/wiki/XSLT) (which is itself a dialect of XML)
-   finally, the translated document must be **displayed by a browser** that understands HTML, like Firefox or Chrome.

Becasue this topic is so immense, we will not be producing fully TEI-compliant documents in this class -- instead, we will make TEI-like XML and process those docs into super-simple HTML documents.

So, in order to complete this assignment, you must learn at least a tiny bit about **XML**, **XSLT**, and **HTML**.  That's a lot! I won't give you a systematic introduction to any of these systems; instead, this handout presents a very small amount of information on each, and gives some examples of how you might use them in the assignment.


### Viewing {#viewing}

To view/work with XML files, please navigate to either of these xml/xslt live editors:

-   [XML fiddle](http://fiddle.frameless.io/) (this one at least has syntax highlighting, which makes the code a bit easier to read).
-   [W3 Schools](https://www.w3schools.com/xml/tryxslt.asp?xmlfile=cdcatalog&xsltfile=cdcatalog) (I don't like this one as much)

**Paste your XML poem into the left window of the editor.** Start with this code:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<poem>
  <l n="1">This <concrete-noun>wall-stone</concrete-noun> is wondrous; fates broke it</l>
  <l n="2"><concrete-noun>courtyard pavements</concrete-noun> were smashed; the work of giants is decaying.</l>
  <l n="3"><concrete-noun>Roofs</concrete-noun> are fallen, ruinous <concrete-noun>towers</concrete-noun>,</l>
  <l n="4"> the frosty gate with frost on cement is ravaged, </l>
</poem>
```

**Paste your XSLT (your script for turning XML into HTML) into the right window of the browser.** Again, here is some starter code:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h1>The Ruin</h1>
        <xsl:for-each select="poem/l/concrete-noun">
          <p> <xsl:value-of select="current()"/> </p>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```


### XML Essentials: Tags & Structures {#xml-essentials-tags-and-structures}

XML "marks up" elements of a text by surrounding bits of text with [tags](https://www.w3schools.com/xml/xml%5Fsyntax.asp). The totality of `<starting-tag>Content</end-tag>` is called an [XML element](https://www.w3schools.com/xml/xml%5Felements.asp).

Take this example (stolen from [W3Schools](https://www.w3schools.com/xml/xml%5Felements.asp)):

```xml
<book category="children">
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```

Here we have a **root element** called `<book>` which encloses several [child elements](https://www.w3schools.com/xml/xml%5Ftree.asp#midcontentadcontainer) (`<title>`, `<author>`, etc). Everything between `<book category="children">` and `</book>` is part of the `<book>` element.  In general, an element has the structure:

-   opening tag: `<tag>`
-   content: text and child elements, which must be fully nexted within the parent (if an opening tag is inside the element, the closing tag must **also** be inside it
-   closing tag: `</tag>` . Note the forward slash **/** within the `<>` greater-than less-than signss.

Here's a trivial example that you might find in a TEI document:

```xml
<l>And then my lord <person>Yvain</person> arrived in <place>Camelot</place>.</l>
```

The tags here are "l", "person", and "place".


#### The XML declaration {#xml-dec}

Every real XML document must also begin with an "XML Declaration" which identifies it as an XML document.  It will look like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

And a very simple full document will look like this:

<a id="code-snippet--simple-xml"></a>
```xml
<?xml version="1.0" encoding="UTF-8"?>
<poem>
  <l n="1">This wall-stone is wondrous; fates broke it</l>
  <l n="2">courtyard pavements were smashed; the work of giants is decaying.</l>
  <l n="3">Roofs are fallen, ruinous towers,</l>
  <l n="4"> the frosty gate with frost on cement is ravaged, </l>
</poem>
```


### Displaying XML with XSLT {#displaying-xml-with-xslt}

A document that has been marked up with XML now has a structure that a computer can understand, which is great! But a web browser will not know how to display that document unless we give it instructions for **transforming** the XML structure into a language that the browser understands. We use XSLT for this purpose -- a special language that exists to manipulate XML documents.

XSLT is complicated, and we will use just a tiny part of it.  We need to understand just a few concepts:

-   **stylesheet declaration** surrounds the rest of the XSLT document, identifying it as an XSLT instruction set
-   **[templates](https://www.w3schools.com/xml/xsl%5Ftemplates.asp)** give instructions for transforming particular XML elements
-   **[Xpath Expressions](https://www.w3schools.com/xml/xpath%5Fsyntax.asp)** are used to tell the templates which elements to transform
-   **value statements** insert the contents of an element into the final HTML product


#### Stylesheet Declaration {#stylesheet-declaration}

An XSLT Stylesheet always starts with an XML declaration and then an `<xsl:stylesheet>` tag; the document ends with the closing `</xsl:stylesheet>` tag:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<!-- Content of Stylesheet Goes Here!! -->

</xsl:stylesheet>
```


#### XSLT Templates {#xslt-templates}

Inside the `xsl:stylesheet` we put all the `xsl:template` tags we need.  Each template is an instruction for dealing with a particular tag or set of tags.  So, if we use [our simple XML file from above](#code-snippet--simple-xml) as the XML source, we might start by building an XSLT document like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
      <xsl:apply-templates/>
  </xsl:template>


  <xsl:template match="l">
    <p> <xsl:value-of select="."/> </p>
  </xsl:template>
</xsl:stylesheet>
```

What's happening here?  We have two templates. The first one "matches" the "root element", while the second one matches all the "l" elements. So if we read this document top to bottom, we might translate it this way:

```text
I am an XML Document

Begin Stylesheet

   Begin Template for the root element
        Apply all Templates!
   End Template for the root elements

   Begin Template for each l element
        Return a line of code that reads:
        "<p> + content of the "l" element + </p>"
        (this creates one HTML paragraph for each "l" element in the original)
   End Template for the L Elements

End Stylesheet
```

Our original XML document is very simple, so we don't need much more than this. But as we'll see later, it can get much more complicated.  And in fact we can make it a little more sophisticated already by adding a bit more complexity:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <body>
      <h1>Grand title</h1>
      <p>Let us begin our discussion of poetry here.</p>
          <xsl:apply-templates/>
    </body>
  </xsl:template>

  <xsl:template match="poem">
    <h2>The Ruin</h2>
          <xsl:apply-templates/>
  </xsl:template>


  <xsl:template match="l">
    <p> <xsl:value-of select="."/> </p>
  </xsl:template>

</xsl:stylesheet>
```

Try to read the text and understand what's going on!

Now let's learn a little bit more about how the `match` and `select` attributes in the above code really work.


#### Xpath Expressions {#xpath-expressions}

When we make templates with a `match` attribute, or use the `value-of` and `apply-templates` instructions (see below), we have to tell XSLT which XML elements we are talking about. The selection of elements is done using what are called "[Xpath Expressions](https://www.w3schools.com/xml/xpath%5Fsyntax.asp)". These are a way to describe the position of elements (sometimes called "nodes") in the XML document. The syntax is extemely complex, so we will just say a few things about it here:

-   "/" refers to the root element -- the element that contains all the other elements in the document
-   `"/poem"` refers to a `<poem>` element **at the document root**, while "poem" refers to **any poem element in the document**.  So for instance, "l" will match all of our `<l>` elements, but `"/l"` **won't match anything,** because the existing `<l>` elements are all _inside the poem element_.
-   "current()" and "." both refer to the **element that is being discussed at the present moment**. So, inside of `<xsl:template match="poem">...</xsl:template>`, `"."` refers to the `<poem>` element.
-   "@n" refers to the "attribute" **n**. I'll explain more about this in a second...


#### Value Statements (`value-of` and `apply-templates`) {#value-statements--value-of-and-apply-templates}

We almost always want to get the value of the XML elements -- otherwise why would we do all this work? There are two ways to get that value...

-    [xsl:value-of](https://www.w3schools.com/xml/ref%5Fxsl%5Fel%5Fvalue-of.asp): the simple way

    `<xsl:value-of select="."/>` just grabs the content of the element and inserts it in the final output.  We don't use it much (see below for reasons), but it can be particularly helpful when we care about **attributes**.  So for instance, consider this line of XML:

    ```xml
    <l n="2">courtyard pavements were smashed; the work of giants is decaying.</l>
    ```

    Maybe we really care that this is line 2! Maybe we want to display those line numbers so readers understand what we're talking about! We can use the "@n" syntax we saw just above:

    ```xml
    <xsl:value-of select="@n"/>
    ```

    When this instruction is applied to the line above, it will return the number "2"!

-    [xsl:apply-templates](https://www.w3schools.com/xml/xsl%5Fapply%5Ftemplates.asp): the better way (usually)

    Most of the time, we use `<xsl:apply-templates/>` instead of `<xsl:value-of select="."/>`.  This is because **we usually can't be sure that the element doesn't contain other elements.** And if we just use "value-of", then the elements inside our current element won't be properly translated.  "apply-templates" will check to see if any templates need to be applied internally, and then after those templates have been applied, it will return the whole resultant text.

    All of this is really helpful -- but since we're generating HTML, you **also** need to know a little bit of HTML to make the text look the way you want it to!


#### HTML Tags and attributes {#html-tags-and-attributes}

I won't go into HTML in much depth -- there are many many _many_ resources available online.  Here we'll just describe a few very basic features.

Like XML documents, HTML documents contain **elements** delimited by **tags**. Also like in XML, those tags can have **attributes** that give extra information.  Here are some tags you may want to use in your work:

```html
<html>
  <body>
    Every HTML document should start with a "html" tag and include a "body" tag inside it.

    <h1>first-level header</h1>
    <h2>second=level header</h2>
    (etc up to "h6")
    <p>
      paragraph containing <strong>bold</strong> and <em>italic</em> text.
      Paragraphs can also contain
      <span>
        tags, which don't do anything by default...
        but wait!
      </span>
    </p>
    <p style="color;white;background-color:red;border:2px solid black; padding: 10px;">
      This paragraph will have white text, a red background, a black border,
      and lots of space around it. Meanwhile, this
      <span style="color:red;background-color:green">
        will be entirely invisible to red-green colorblind readers.
      </span>
    </p>

    <table>
      <tr>
        <td>this is a </td>
        <td>table with</td>
        <td>1 row and 3 columns</td>
      </tr>
    </table>


  </body>
</html>
```

-   **p** tags are paragraphs
-   **h1, h2... h6** tags are headers
-   **span** tags delineate text within a paragraph
-   **strong** and **em** do bold and italics
-   You can build tables using the somewhat complicated syntax above
-   you can set style attributes using the "style=" commands as you see them above; I've shown a few possibilities but there are literally hundreds more.

Hopefully this should be enough for you to get started!


### Learn more {#learn-more}

The [Mozilla Developer Network](https://developer.mozilla.org) is the best starting point for almost all technical topics related to the web.  The [XML Introduction](https://developer.mozilla.org/en-US/docs/Web/XML/XML%5Fintroduction), [XSLT Intro](https://developer.mozilla.org/en-US/docs/Web/XSLT), and [much more extensive HTML information](https://developer.mozilla.org/en-US/docs/Web/HTML) are all very helpful, and contian links to further information.

The [TEI website](https://tei-c.org/) has extensive information about the TEI standard, but is extremely technical. [TEI By Example](http://teibyexample.org/modules/TBED04v00.htm) can be quite helpful, but again, is very detailed.  The full text of _[What is the Text Encoding Initiative](https://books.openedition.org/oep/426)_ is available online and may also be helpful. The University of Nebraska's  [Basic Guide to Text Encoding](https://cdrh.unl.edu/articles/basicguide) is a lightweight introduction that may be easier to follow than any of the above!


## Reading Hints {#reading}

-   Content: Read your passage. Flag any parts that are unclear or mysterious or confusing. Summarize its content in one sentence.
-   Style: Look for:
    -   verbal patterns (e.g. sentences with the same shape) : what are they? What is their effect?
    -   sensory imagery (e.g. references to what you can see, hear, touch, feel): any patterns? What do they do for the poem?
-   Theme: if you had to summarize the theme of your passage in one word, what would that word be? How does style support or embody theme?


## Encoding {#encoding}

**Choose one of the following passages:** 1-15; 16-31a; 31b-46.

Encode your passage using the following TEI tags:

-   **Lines and line numbers**

<!--listend-->

```xml
 <poem>
   <l n=″1″>This masonry is wondrous; fates broke it</l>
</poem>
```

-   **At least one made-up tag of your own, specific to the poem**

<!--listend-->

```xml
<concrete_noun> wall-stone </concrete_noun>
<adjective> wondrous </adjective>
<colour>golden</colour>
<poetic-formula>the work of giants</thew
```


## Encoding Discussion {#encoding-discussion}

What is your made-up tag(s)? How is this tag supposed to work, within this poem and more generally? Why is it useful?

After encoding, what additional characteristics of the poem, if any, did you notice in terms of verbal patterns, sensory imagery, or the development of the poem's themes?


## Appendix: More Complex Example {#appendix-more-complex-example}

It may help you to see a few more tags. Here is a slightly more complex example, with a more completely marked-up selection of the poem. I have **not** annotated this example, but it showcases a few more features of the systems we're learning.  In particular, this example introduces:

-   [more complex colors](https://www.w3schools.com/cssref/css%5Fcolors%5Flegal.asp)
-   [the "a" or hyperlink tag](https://www.w3schools.com/tags/tag%5Fa.asp)
-   [curly braces as a shortcut for xpaths](https://stackoverflow.com/questions/10395488/how-to-concat-a-string-to-xslvalue-of-select)
-   [the somewhat confusing xpath test "node"](https://stackoverflow.com/questions/11744465/xpath-difference-between-node-and-text), which sometimes makes sense to use when "current()" doesn't produce the effect you want.

<!--listend-->

```xml
<?xml version="1.0" encoding="UTF-8"?>
<poem>
  <l n="1">This <concrete-noun>wall-stone</concrete-noun> is <adjective>wondrous</adjective>; <hyperbole>fates broke it</hyperbole></l>
  <l n="2"><concrete-noun>courtyard pavements</concrete-noun> were smashed; the <concrete-noun>work</concrete-noun> of <concrete-noun>giants</concrete-noun> is decaying.</l>
  <l n="3"><concrete-noun>Roofs</concrete-noun> are fallen, ruinous <concrete-noun>towers</concrete-noun>,</l>
  <l n="4"> the frosty <concrete-noun>gate</concrete-noun> with <concrete-noun>frost</concrete-noun> on <concrete-noun>cement</concrete-noun> is <hard-word>ravaged</hard-word>, </l>
</poem>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <body>
        <h1>The Ruin</h1>
        <table>
          <xsl:apply-templates select="node()"/>
        </table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="poem">
    <table>
      <xsl:apply-templates select="node()"/>
    </table>
  </xsl:template>

  <xsl:template match="l">
    <tr>
      <td style="padding-right:10px; color:gray">
        <xsl:value-of select="@n"/>
      </td>
      <td style="color:white;">
        <xsl:apply-templates select="node()"/>
      </td>
    </tr>
  </xsl:template>

  <xsl:template match="concrete-noun">
    <strong style="color:black;">
      <xsl:apply-templates select="node()"/>
    </strong>
  </xsl:template>
  <xsl:template match="adjective">
    <span style="color:green">
      <xsl:apply-templates select="node()"/>
    </span>
  </xsl:template>

  <xsl:template match="hyperbole">
    <span style="background-color: rgba(250,20,20,0.3)">
      <xsl:apply-templates select="node()"/>
    </span>
  </xsl:template>

  <xsl:template match="hard-word">
    <a style="background-color: rgba(20,250,20,0.3)" href="https://www-oed-com.myaccess.library.utoronto.ca/search?q={current()}">
      <xsl:apply-templates select="node()"/>
    </a>
  </xsl:template>

</xsl:stylesheet>
```
