This is a running encyclopedia of research into fundamental physics.

It should be linked together like a wiki.

The point of doing research this way is to build up "modular thought" -- where modules are encapsulated, and dependencies are clean.

## modules

Each module has an "entry.md" which is the "entry point" summary of that module's main idea.

It must start with an h1 title, and be immediately followed by a compact paragraph that summarizes it.  The rest of the structure is free-form.

The module can contain as many resources as are appropriate.  They may be markdown, python scripts, data sets, pdfs, images, whatever.

The purpose of a module is that it contains "1 main idea" (which is sometimes rather large).  And then can have surrounding resources which help break up the monolith.

### authoring

BEWARE AI SLOP!

**Do not** write things like:
- table of contents (especially in the "entry.md" file)
- manual backlinks (eg, "this note is used by that other one")
- boilerplate commentary or meta-analysis
- summaries of summaries

Things like backlinks & table-of-contents can be derived automatically with a program like Obsidian.  And a summary-of-a-summary is pointless - an AI agent can just read the first 1,000 words of the source material.  Context windows are not that scarce.

**Do** this:
- try to write a clear summary at a markdown's note content at the top.  This helps economize search.
- explore for duplicate content, and abstract out shared modules


If the content has a clear dependency order of small, modular notes, feel free to write a master markdown note that "synthesizes" the encapsulated dependencies in order.  This is writing in the style of Spinoza or Euclid, where an ordered flow of modular statements build on each other.  That is a fine way to write.  It can even go in the "entry.md" file, which acts as the master synthesis.   Of course, not every module is making a structured argument - but do consider this when appropriate.

### Markdown is the best, PDFs are bad

When authoring long-form content, always prefer Markdown.  LaTeX is not as good.  PDFs are horrible.  I never want PDFs to be authored.  I will type-set and print on my own.  Write in Markdown because that is easiest to parse.

### immutable logs

It is ok to have junk drawers of immutable material.  Logs of conversations, false starts, morgue, rough material that got refined later.  Don't be shy about creating a "./junk-drawer" directory, and put things in there for cold storage.

## Inbox directory

The "./inbox" is unprocessed raw content.  It should not be polished in place, but woven into other modules.

## Chat history

Sometimes a directory will have a sub-directory called `./chats`.

That directory is meant as a historical log of the discussion that surrounded the main content of that directory's theme.

Conventionally, the `./chats` directory will have numerically ordered sub-directories (01, 02, 03).  Inside each there will be the "prompt.md" and "response.md".  There may also be "attachments/" (which were offered in the prompt) and outputs (which were produced by the response).