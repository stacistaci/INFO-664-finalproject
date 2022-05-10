# W.S. Merwin bot

This project uses [GPT-2](https://openai.com/blog/better-language-models/) to generate new text in the style of poet W.S. Merwin. The generated text is organized into four-line "stanzas," which then get published on Twitter bot [@wsmerwin_bot](https://twitter.com/wsmerwin_bot) using AWS Lambda.

## Data
W.S. Merwin was a highly prolific poet, although most of his work is not available online. I had hoped to scrape Poetry Foundation and The New Yorker for text, but most of his poems in both places were only available as scanned PDFs of magazine or book pages (i.e., not scrapable). I came across [this old Poetry Foundation scraper](https://github.com/eli8527/poetryfoundation-scraper) that no longer works, but has a .txt file of previously scraped W.S. Merwin poems. On top of that, I was able to scrape the ~20 or so more recent poems from [The New Yorker](https://www.newyorker.com/contributors/w-s-merwin) that are available as readable text (published before ~2007). Combining the two sources, I ended up with almost 400 poems to finetune the GPT-2 model.

## GPT-2
I used Max Woolf's [GPT-2 simple](https://github.com/minimaxir/gpt-2-simple) package for finetuning models and text generation. For access to a GPU, I ran the model on a pro Colab account. I then bulk generated text using the finetuned model, split the text into four-line "stanzas" and saved them as a json file.

## Twitter bot
After creating a dev account on Twitter, I used Tweepy to post updates via the Twitter API. Finally, I used AWS Lambda to run the code serverless, on a schedule of every 12 hours.

