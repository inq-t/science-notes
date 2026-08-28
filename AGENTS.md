This is a running encyclopedia of research into fundamental physics.

I am philosopher first, a computer scientist second, a mathematician third, and a physicist fourth.

I prefer precision of distinctions, like Duns Scotus and Thomas Aquinas.  I prefer thinking deeply about essential structures and grounding reasons like Heidegger and Leibniz.  And I prefer clarity of presentation like Kant and Spinoza.

But I want rigorous mathematical notation.  If we go far enough, we will have to invent our own mathematics.

## motto

Physics is math.
There is a reason for everything.
"Why is there something rather than nothing" must have an answer.  And if the answer is true, it necessitates something.

The structure, not the measure, of nature is its essence.  And that essence is necessary - not an empty possibility.  At some deep level, the conditions for the possibility of nature are identical to its necessity.

The only way to get at this is to interrogate the fundamentals of what makes algebra possible.

Cosmology is not the measurement of the cosmos, but the study of what makes a cosmos a cosmos.  A cosmos is the arena of facts.
## thinking in graphs

It should be linked together like a wiki.

The point of doing research this way is to build up "modular thought" -- where modules are encapsulated, and dependencies are clean.

## modules

Each module has an `inq.md` whose body is the entry-point summary of that module's main idea.

It must start with an h1 title, and be immediately followed by a compact paragraph that summarizes it.  The rest of the structure is free-form.

The module can contain as many resources as are appropriate.  They may be markdown, python scripts, data sets, pdfs, images, whatever.

The purpose of a module is that it contains "1 main idea" (which is sometimes rather large).  And then can have surrounding resources which help break up the monolith.

### authoring

BEWARE AI SLOP!

**Do not** write things like:
- table of contents (especially in the `inq.md` file)
- manual backlinks (eg, "this note is used by that other one")
- boilerplate commentary or meta-analysis
- summaries of summaries

Things like backlinks & table-of-contents can be derived automatically with a program like Obsidian.  And a summary-of-a-summary is pointless - an AI agent can just read the first 1,000 words of the source material.  Context windows are not that scarce.

**Do** this:
- try to write a clear summary at a markdown's note content at the top.  This helps economize search.
- explore for duplicate content, and abstract out shared modules


If the content has a clear dependency order of small, modular notes, feel free to write a master markdown note that "synthesizes" the encapsulated dependencies in order.  This is writing in the style of Spinoza or Euclid, where an ordered flow of modular statements build on each other.  That is a fine way to write.  It can even go in the `inq.md` body, which acts as the master synthesis.   Of course, not every module is making a structured argument - but do consider this when appropriate.

### Markdown is the best, PDFs are bad

When authoring long-form content, always prefer Markdown.  LaTeX is not as good.  PDFs are horrible.  I never want PDFs to be authored.  I will type-set and print on my own.  Write in Markdown because that is easiest to parse.

### immutable logs

It is ok to have junk drawers of immutable material.  Logs of conversations, false starts, morgue, rough material that got refined later.  Don't be shy about creating a "./junk-drawer" directory, and put things in there for cold storage.

## Library Directory

Articles from other authors are kept in the "library/".  Each article deserves its own "module".  The entry note should be little more than the abstract of the article.  Prefer to keep the LaTeX and machine-readable resources for the article.  PDFs are useless garbage compared to LaTeX.

DO NOT add commentary in the library.  Commentary and analysis should go in other modules that consume the "raw" library articles.

## Inbox directory

The "./inbox" is unprocessed raw content.  It should not be polished in place, but woven into other modules.

## Chat history

Sometimes a directory will have a sub-directory called `./chats`.

That directory is meant as a historical log of the discussion that surrounded the main content of that directory's theme.

Conventionally, the `./chats` directory will have numerically ordered sub-directories (01, 02, 03).  Inside each there will be the "prompt.md" and "response.md".  There may also be "attachments/" (which were offered in the prompt) and outputs (which were produced by the response).
