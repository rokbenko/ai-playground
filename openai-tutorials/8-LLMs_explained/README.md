# #8 LLMs explained

<br>

## 📖 Description 📖

Python and Node.js examples on how LLMs work using the OpenAI SDK `top_logprobs` parameter.

<br>

## 🧠 Learning goal 🧠

- **Understanding LLMs:** By utilizing parameters `logprobs` and `top_logprobs`, we can see exactly which tokens the LLM considered at each step of generating a response and how confident it was about each option. This insight provides a more practical understanding of how LLMs predict the next word based on context. LLMs are designed to predict the next token in a sequence, using prior tokens to guide their choices. With the `logprobs` parameter set to `True`/`true`, the LLM returns the log probabilities for each token in the response. By adding the `top_logprobs` parameter, we can examine the top N most likely tokens the LLM considered and the likelihood of each.

<br>

## 🔥 Working examples in Python and Node.js 🔥

If you run [llms_explained.py](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/8-LLMs_explained/llms_explained.py) or [llms_explained.js](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/8-LLMs_explained/llms_explained.js), you should get the following response:

> Chosen token: "Albert"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: "Albert"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -0.00034619053<br>
> 2. Token: "Ein"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -8.000346<br>     
> 3. Token: "Al"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -11.500346<br>    
> 4. Token: "He"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -15.625346<br>    
> 5. Token: "A"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -16.000347<br>    
> 
> <br>
> 
> Chosen token: " Einstein"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " Einstein"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: 0.0<br>
> 2. Token: "Ein"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -19.125<br>       
> 3. Token: " ein"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -19.75<br>        
> 4. Token: " Ein"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -20.125<br>
> 5. Token: " E"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -21.25<br>
> 
> <br>
> 
> Chosen token: " was"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " was"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -3.650519e-06<br>
> 2. Token: " is"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -12.875004<br>
> 3. Token: " developed"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -14.375004<br>
> 4. Token: "was"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -16.000004<br>
> 5. Token: " был"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -16.125004<br>
> 
> <br>
> 
> Chosen token: " a"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " a"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -1.3856493e-06<br>
> 2. Token: " an"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -14.375001<br>
> 3. Token: " renowned"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -14.500001<br>
> 4. Token: " the"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -16.000002<br>
> 5. Token: " one"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -16.375002<br>
> 
> <br>
> 
> Chosen token: " theoretical"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " theoretical"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -0.052820187<br>
> 2. Token: " renowned"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -3.1778202<br>
> 3. Token: " groundbreaking"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -5.42782<br>
> 4. Token: " revolutionary"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -6.05282<br>
> 5. Token: " physic"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -6.30282<br>
> 
> <br>
> 
> Chosen token: " physic"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " physic"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -1.9361265e-07<br>
> 2. Token: " physics"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -16.625<br>
> 3. Token: "phys"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -16.875<br>
> 4. Token: " phys"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -17.375<br>
> 5. Token: " Phys"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -17.375<br>
> 
> <br>
> 
> Chosen token: "ist"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: "ist"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: 0.0<br>
> 2. Token: "ists"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -19.25<br>
> 3. Token: "st"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -24.375<br>
> 4. Token: "ista"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -24.375<br>
> 5. Token: "iste"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -25.0<br>
> 
> <br>
> 
> Chosen token: " known"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " known"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -0.08508552<br>
> 2. Token: " best"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -2.8350856<br>
> 3. Token: " renowned"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -3.8350856<br>
> 4. Token: " famous"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -6.8350854<br>
> 5. Token: " who"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -9.210086<br>
> 
> <br>
> 
> Chosen token: " for"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " for"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -1.0280384e-06<br>
> 2. Token: " primarily"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -13.875001<br>
> 3. Token: " mainly"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -17.500002<br>
> 4. Token: " best"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -18.250002<br>
> 5. Token: " mostly"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -18.750002<br>
> 
> <br>
> 
> Chosen token: " the"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " developing"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -0.5058654<br>
> 2. Token: " the"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -1.6308653<br>
> 3. Token: " his"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -1.6308653<br>
> 4. Token: " form"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -5.2558656<br>
> 5. Token: " proposing"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -8.880865<br>
> 
> <br>
> 
> Chosen token: " theory"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " theory"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -0.00033248574<br>
> 2. Token: " theories"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -8.750333<br>
> 3. Token: " Theory"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -8.875333<br>
> 4. Token: " development"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -10.875333<br>
> 5. Token: "Theory"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -12.000333<br>
> 
> <br>
> 
> Chosen token: " of"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " of"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: 0.0<br>
> 2. Token: "of"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -22.625<br>
> 3. Token: " relat"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -24.75<br>
> 4. Token: "_of"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -24.875<br>
> 5. Token: " של"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -25.375<br>
> 
> <br>
> 
> Chosen token: " relat"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: " relat"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -6.6306106e-06<br>
> 2. Token: " general"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -12.250007<br>
> 3. Token: " relativ"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -13.375007<br>
> 4. Token: " relatively"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -16.250006<br>
> 5. Token: " Rel"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -17.000006<br>
> 
> <br>
> 
> Chosen token: "ivity"<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: "ivity"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: 0.0<br>
> 2. Token: "IVITY"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -20.625<br>
> 3. Token: "ativity"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -20.875<br>
> 4. Token: "iveness"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -21.125<br>
> 5. Token: "avity"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -22.0<br>
> 
> <br>
> 
> Chosen token: "."<br>
> ----------------------------------------<br>
> Top logprobs:<br>
> 1. Token: "."<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -2.3392786e-06<br>
> 2. Token: ".<br>
> "<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -13.125002<br>
> 3. Token: " and"<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -15.875002<br>
> 4. Token: ".<br>
> &nbsp;<br>
> "<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -16.000002<br>
> 5. Token: ","<br>
> &nbsp;&nbsp;&nbsp;&nbsp;Log probability: -18.250002<br>

<br>

## ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8` or [Node.js](https://nodejs.org/en) `21.2.0`
- [OpenAI Python SDK](https://pypi.org/project/openai/) `1.45.1` or [OpenAI Node.js SDK](https://www.npmjs.com/package/openai) `4.61.1`
