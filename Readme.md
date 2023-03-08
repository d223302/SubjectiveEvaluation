# Supplementary material for the paper **Why We Should Report the Details in Subjective Evaluation of TTS More Rigorously**

## Full list of surveyed paper

The following table is the 88 paper we survey; all of them are from [INTERSPEECH 2022](https://www.isca-speech.org/archive/interspeech_2022/index.html).
In the table, the `v` means that the paper reports the factor, and `x` means that the paper do not report the factor.
The column *# of raters and rated items* considers four factors: (1) the total number of unique raters, (2) the number of samples a rater rates, (3) how many raters evaluate a single sample, and (4) how many audio samples in total. 
If the paper report none of the four factors, we put a `x`; if the paper report all four factors, we put a `v`; if the paper report some but not all the four factors, we put a `△`.
For the column *Instruction*, we check if the paper provides either the rating scales or the questions presented to the evaluators.
For the column *Increment*, we check if the paper uses a 1-point increment or 0.5-point increment in the MOS tests.
For those we cannot know what increment the paper uses, we put a `x`.
Some paper just say *"from 1~5"*, but this description is too vague for us to know if it is an 1-increment or a 0.5-increment, so we still put a `x` in this case.
For the papers that do not conduct a MOS test, we just put a `-` in the *Increment* field.


| Title | Platform | Qualification | Post-filter | Language background | Location | # of raters and rated items | Payment | Instructions | Increment (MOS)|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|SANE-TTS: Stable And Natural End-to-End Multilingual Text-to-Speech | Mturk | x | x | v | x | △ | x | x | 1|
|Enhancement of Pitch Controllability using Timbre-Preserving Pitch Augmentation in FastPitch  | x | x | x | v | x | △ | x | v | 1|
|Speaking Rate Control of end-to-end TTS Models by Direct Manipulation of the Encoder’s Output Embeddings | Prolific | x | x | x | x | v | x | v | v|
|TriniTTS: Pitch-controllable End-to-end TTS without External Aligner | Mturk | x | x | x | x | △ | x | x | x|
|JETS: Jointly Training FastSpeech2 and HiFi-GAN for End to End Text to Speech  | Mturk | x | x | x | v | △ | x | v | 1|
|EdiTTS: Score-based Editing for Controllable Text-to-Speech | Mturk | x | x | x | x | △ | x | x | 1|
|SpeechPainter: Text-conditioned Speech Inpainting Zalan Borsos | x | x | x | x | x | △ | x | v | 1|
|Neural Lexicon Reader: Reduce Pronunciation Errors in End-to-end TTS by Leveraging External Textual Knowledge | x | x | x | x | x | △ | x | x | x|
|DocLayoutTTS: Dataset and Baselines for Layout-informed Document-level Neural Speech Synthesis  | x | x | x | v | x | △ | x | x | 0.5|
|Mixed-Phoneme BERT: Improving BERT with Mixed Phoneme and Sup-Phoneme Representations for Text to Speech | x | x | x | v | x | △ | x | x | x|
|An Efficient and High Fidelity Vietnamese Streaming End-to-End Speech Synthesis  | x | x | x | v | v | △ | x | x | x|
|Environment Aware Text-to-Speech Synthesis | x | x | x | x | x | △ | x | x | v|
|A Study of Modeling Rising Intonation in Cantonese Neural Speech Synthesis  | x | x | x | v | x | △ | x | x | x|
|Transfer Learning Framework for Low-Resource Text-to-Speech using a Large-Scale Unlabeled Speech | x | x | x | x | x | △ | x | x | 1|
|DRSpeech: Degradation-Robust Text-to-Speech Synthesis with Frame-Level and Utterance-Level Acoustic Representation Learning | x | x | x | x | x | △ | x | x | x|
|MSR-NV: Neural Vocoder Using Multiple Sampling Rates | x | v | x | x | x | △ | x | x | v|
|SpecGrad: Diffusion Probabilistic Model based Neural Vocoder with Adaptive Noise Spectral Shaping  | x | x | x | v | v | △ | v | v | 1|
|Bunched LPCNet2: Efficient Neural Vocoders Covering Devices from Cloud to Edge | Mturk | x | x | x | x | △ | x | v | 1|
|Hierarchical and Multi-Scale Variational Autoencoder for Diverse and Natural Non-Autoregressive Text-to-Speech  | x | x | x | v | x | △ | x | x | x|
|End-to-end LPCNet: A Neural Vocoder With Fully-Differentiable LPC Estimation' | x | x | x | x | x | △ | x | v | 1|
|WavThruVec: Latent speech representation as intermediate features for neural speech synthesis  | Mturk | v | x | x | v | △ | x | x | 1|
|Fast Grad-TTS: Towards Efficient Diffusion-Based Speech Generation on CPU  | Mturk | v | x | x | x | △ | x | x | 0.5|
|Simple and Effective Unsupervised Speech Synthesis  | Mturk | x | x | x | x | △ | x | x | 1|
|Unified Source-Filter GAN with Harmonic-plus-Noise Source Excitation Generation | x | x | x | x | x | △ | x | x | x|
|Speaker Attractor Text to Speech, Learning to Speak by Learning to Separate | x | x | x | x | x | △ | x | v | 0.5|
|End-to-End Binaural Speech Synthesis  | x | x | x | x | x | x | x | x | v|
|PoeticTTS - Controllable Poetry Reading for Literary Studies | x | x | x | x | x | △ | x | x | v|
|A Multi-Scale Time-Frequency Spectrogram Discriminator for GAN-based Non-Autoregressive TTS  | Mturk | x | x | x | x | △ | x | x | x|
|RetrieverTTS: Modeling Decomposed Factors for Text-Based Speech Insertion | x | x | x | x | x | △ | x | x | x|
|FlowVocoder: A small Footprint Neural Vocoder based Normalizing Flow for Speech Synthesis | x | x | x | x | x | △ | x | x | 1|
|DelightfulTTS 2: End-to-End Speech Synthesis with Adversarial Vector-Quantized Auto-Encoders  | x | x | v | x | x | △ | x | x | 0.5|
|AdaVocoder: Adaptive Vocoder for Custom Voice  | x | x | x | x | x | △ | x | x | x|
|RefineGAN: Universally Generating Waveform Better than Ground Truth with Highly Accurate Pitch and Intensity Responses | x | x | x | x | x | △ | x | x | x|
|VQTTS: High-Fidelity Text-to-Speech Synthesis with Self-Supervised VQ Acoustic Feature  | x | x | x | x | x | △ | x | x | x|
|IMPROVING GAN-BASED VOCODER FOR FAST AND HIGH-QUALITY SPEECH SYNTHESIS  | x | x | x | v | x | △ | x | v | x|
|SoftSpeech: Unsupervised Duration Model in FastSpeech 2 | x | x | x | x | x | △ | x | v | 1|
|A Multi-Stage Multi-Codebook VQ-VAE Approach to High-Performance Neural TTS  | x | x | x | x | x | △ | x | x | 0.5|
|Text-to-speech synthesis using spectral modeling based on non-negative autoencoder | x | x | x | x | x | △ | x | x | v|
|Joint Modeling of Multi-Sample and Subband Signals for Fast Neural Vocoding on CPU | x | x | x | x | x | △ | x | v | 1|
|MISRNet: Lightweight Neural Vocoder Using Multi-Input Single Shared Residual Blocks | x | x | x | x | x | △ | x | v | 1|
|A compact transformer-based GAN vocoder | x | x | x | x | x | △ | x | x | x|
|Diffusion Generative Vocoder for Fullband Speech Synthesis Based on Weak Third-order SDE Solver | x | x | x | x | x | x | v | x | x|
|From Start to Finish: Latency Reduction Strategies for Incremental Speech Synthesis in Simultaneous Speech-to-Speech Translation | Mturk | x | x | x | x | △ | x | x | x|
| Unified Accent Estimation Method Based on Multi-Task Learning for Japanese Text-to-Speech  | x | x | x | v | x | △ | x | v | 1|
|Vocal effort modeling in neural TTS for improving the intelligibility of synthetic speech in noise  | x | x | x | v | v | △ | x | x | x|
|TTS-by-TTS 2: Data-selective augmentation for neural speech synthesis using ranking support vector machine with variational autoencoder | x | x | x | v | v | △ | x | x | x|
|Glow-WaveGAN 2: High-quality Zero-shot Text-to-speech Synthesis and Any-to-any Voice Conversion | x | x | x | x | x | △ | x | x | x|
|Content-Dependent Fine-Grained Speaker Embedding for Zero-Shot Speaker Adaptation in Text-to-Speech Synthesis | x | x | x | v | x | △ | x | x | 1|
|CopyCat2: A Single Model for Multi-Speaker TTS and Many-to-Many Fine-Grained Prosody Transfer  | x | x | x | v | v | v | x | v | v|
|Simple and Effective Multi-sentence TTS with Expressive and Coherent Prosody  | x | x | x | x | x | v | x | v | v|
|Acoustic Modeling for End-to-End Empathetic Dialogue Speech Synthesis Using Linguistic and Prosodic Contexts of Dialogue History | x | x | x | x | x | △ | x | x | v|
|Emphasis Control for Parallel Neural TTS | x | x | x | v | v | △ | x | v | 1|
|BERT, can HE predict contrastive focus? Predicting and controlling prominence in neural TTS using a language model | Prolific | x | x | v | x | △ | x | x | v|
|Combining conversational speech with read speech to improve prosody in Text-to-Speech synthesis | Prolific | v | v | v | v | △ | x | v | 1|
|Exploring Timbre Disentanglement in Non-Autoregressive Cross-Lingual Text-to-Speech | x | x | x | v | x | △ | x | x | 0.5|
|WeSinger: Data-augmented Singing Voice Synthesis with Auxiliary Losses  | x | x | x | x | x | △ | x | x | x|
|Decoupled Pronunciation and Prosody Modeling in Meta-Learning-based Multilingual Speech Synthesis  | Mturk | x | x | v | x | △ | x | v | 1|
|KaraTuner: Towards End-to-End Natural Pitch Correction for Singing Voice in Karaoke | x | x | x | x | x | △ | x | x | x|
|Learn2Sing 2.0: Diffusion and Mutual Information-Based Target Speaker SVS by Learning from Singing Teacher | x | x | x | x | x | x | x | x | x|
|SingAug: Data Augmentation for Singing Voice Synthesis with Cycle-consistent Training Strategy  | x | v | x | x | x | △ | x | v | 1|
|Muskits: an End-to-end Music Processing Toolkit for Singing Voice Synthesis | x | v | x | x | x | △ | x | v | 1|
|Pronunciation Dictionary-Free Multilingual Speech Synthesis by Combining Unsupervised and Supervised Phonetic Representations | x | x | x | v | x | △ | x | x | 0.5|
|Towards High-fidelity Singing Voice Conversion with Acoustic Reference and Contrastive Predictive Coding | x | v | x | x | x | △ | x | v | 1|
|Towards Improving the Expressiveness of Singing Voice Synthesis with BERT Derived Semantic Information  | x | x | x | v | x | △ | x | x | 1|
|Normalization of code-switched text for speech synthesis  | x | x | x | v | x | △ | x | x | x|
|Synthesizing Near Native-accented Speech for a Non-native Speaker by Imitating the Pronunciation and Prosody of a Native Speaker | Mturk | x | x | v | x | △ | x | x | 1|
| A Hierarchical Speaker Representation Framework for One-shot Singing Voice Conversion | x | x | x | x | x | △ | x | x | x|
| Expressive, Variable, and Controllable Duration Modelling in TTS | x | x | x | v | x | △ | x | x | v|
|Predicting VQVAE-based Character Acting Style from Quotation-Annotated Text for Audiobook Speech Synthesis | x | x | x | x | x | △ | x | x | x|
|Adversarial and Sequential Training for Cross-lingual Prosody Transfer TTS | x | x | x | x | x | x | x | x | x|
|FluentTTS: Text-dependent Fine-grained Style Control for Multi-style TTS | x | x | x | x | x | △ | x | v | x|
|Few Shot Cross-Lingual TTS Using Transferable Phoneme Embedding | x | x | x | x | x | △ | x | x | x|
|Training Text-To-Speech Systems From Synthetic Data: A Practical Approach For Accent Transfer Tasks  | x | x | x | x | x | x | x | v | 1|
|Spoken-Text-Style Transfer with Conditional Variational Autoencoder and Content Word Storage  | x | x | x | v | x | △ | x | x | v|
|Analysis of expressivity transfer in non-autoregressive end-to-end multispeaker TTS systems | x | x | x | x | v | △ | x | x | x|
|Cross-lingual Style Transfer with Conditional Prior VAE and Style Loss | x | x | x | x | x | △ | x | v | v|
|Daft-Exprt: Cross-Speaker Prosody Transfer on Any Text for Expressive Speech Synthesis  | x | x | v | v | x | △ | x | x | x|
|Language Model-Based Emotion Prediction Methods for Emotional Speech Synthesis Systems  | x | x | x | v | x | △ | x | v | 1|
|Text aware Emotional Text-to-speech with BERT | x | x | x | v | x | △ | x | v | x|
|Transplantation of Conversational Speaking Style with Interjections in Sequence-to-Sequence Speech Synthesis | x | v | x | x | x | △ | x | x | x|
|Cross-speaker Emotion Transfer Based On Prosody Compensation for End-to-End Speech Synthesis  | x | x | x | v | x | △ | x | v | 1|
|Self-supervised Context-aware Style Representation for Expressive Speech Synthesis  | UHRS | x | x | x | x | △ | x | v | x|
|Automatic Prosody Annotation with Pre-Trained Text-Speech Model | x | x | x | x | x | △ | x | v | 1|
|Enhancing Word-Level Semantic Representation via Dependency Structure for Expressive Text-to-Speech Synthesis  | x | v | x | x | x | △ | x | x | x|
|Towards Multi-Scale Speaking Style Modelling with Hierarchical Context Information for Mandarin Speech Synthesis  | x | x | x | v | x | △ | x | x | 1|
|Towards Cross-speaker Reading Style Transfer on Audiobook Dataset  | x | x | x | v | x | △ | x | x | x|
|CALM: Constrastive Cross-modal Speaking Style Modeling for Expressive Text-to-Speech Synthesis | x | x | x | v | x | △ | x | x | 1|
|Improve emotional speech synthesis quality by learning explicit and implicit representations with semi-supervised training | x | x | x | v | x | △ | x | x | 0.5|


## Audio files used in our crowdsourcing experiments
