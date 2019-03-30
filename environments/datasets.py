DATASETS = {
        "imdb": {
            "train": "s3://suching-dev/final-datasets/imdb/train_pretokenized.jsonl",
            "dev": "s3://suching-dev/final-datasets/imdb/dev_pretokenized.jsonl",
            "test": "s3://suching-dev/final-datasets/imdb/test_pretokenized.jsonl",
            "unlabeled": "s3://suching-dev/final-datasets/imdb/unlabeled_pretokenized.jsonl",
            "reference_counts":  "s3://suching-dev/final-datasets/imdb/valid_npmi_reference/train.npz",
            "reference_vocabulary":  "s3://suching-dev/final-datasets/imdb/valid_npmi_reference/train.vocab.json",
            "stopword_path": "s3://suching-dev/stopwords/snowball_stopwords.txt",
            "glove": {
                "in-domain": "s3://suching-dev/pretrained-models/glove/imdb_300/vectors.txt",
                "out-domain": "https://s3-us-west-2.amazonaws.com/allennlp/datasets/glove/glove.840B.300d.txt.gz"
            },
            "elmo": {
                "frozen": "s3://allennlp/models/transformer-elmo-2019.01.10.tar.gz",
                "fine-tuned": "s3://suching-dev/pretrained-models/elmo/imdb/model.tar.gz",
                "in-domain": "s3://suching-dev/pretrained-models/in-domain-elmo/imdb/model.tar.gz"
            },
            "bert": {
                "frozen": {
                    "weights": "bert-base-uncased",
                    "vocab": "bert-base-uncased",
                },
                "fine-tuned": {
                    "weights": "s3://suching-dev/pretrained-models/bert/imdb/model.tar.gz",
                    "vocab": "s3://suching-dev/pretrained-models/bert/imdb/vocab.txt"
                }
            },
            "vae": {
                "model_archive": "/Users/suching/Github/vae/model_logs/ft_w_pretrained/model.tar.gz",
                "vocab": "/Users/suching/Github/vae/model_logs/ft_w_pretrained/vocabulary/vae.txt",
                "bg_freq": "/Users/suching/Github/vae/model_logs/ft_w_pretrained/vocabulary/vae.bgfreq.json"
            }
        },
        "1b": {
            "train": "s3://suching-dev/final-datasets/1b/train.jsonl",
            "test": "s3://suching-dev/final-datasets/1b/test.jsonl",
            "reference_counts":  "s3://suching-dev/final-datasets/1b/test_npmi_reference/train.npz",
            "reference_vocabulary":  "s3://suching-dev/final-datasets/1b/test_npmi_reference/train.vocab.json",
            "stopword_path": "s3://suching-dev/stopwords/snowball_stopwords.txt",
            "glove": {
                "in-domain": "s3://suching-dev/pretrained-models/glove/1b_300/vectors.txt",
                "out-domain": "https://s3-us-west-2.amazonaws.com/allennlp/datasets/glove/glove.840B.300d.txt.gz"
            },
            "elmo": {
                "frozen": "s3://allennlp/models/transformer-elmo-2019.01.10.tar.gz",
                "fine-tuned": "s3://suching-dev/pretrained-models/elmo/1b/model.tar.gz",
                "in-domain": "s3://suching-dev/pretrained-models/in-domain-elmo/1b/model.tar.gz"
            },
            "bert": {
                "frozen": {
                    "weights": "bert-base-uncased",
                    "vocab": "bert-base-uncased",
                },
                "fine-tuned": {
                    "weights": "s3://suching-dev/pretrained-models/bert/1b/model.tar.gz",
                    "vocab": "s3://suching-dev/pretrained-models/bert/1b/vocab.txt"
                }
            },
            "vae": {
                "model_archive": "s3://suching-dev/pretrained-models/vae_best_npmi/1b/model.tar.gz",
                "vocab": "s3://suching-dev/pretrained-models/vae_best_npmi/1b/vae.txt",
                "bg_freq": "s3://suching-dev/pretrained-models/vae_best_npmi/1b/vae.bgfreq.json"
            }
        },
        "amazon": {
            "train": "s3://suching-dev/final-datasets/amazon/train.jsonl",
            "dev": "s3://suching-dev/final-datasets/amazon/dev.jsonl",
            "test": "s3://suching-dev/final-datasets/amazon/test.jsonl",
            "unlabeled": "s3://suching-dev/final-datasets/amazon/unlabeled.jsonl",
            "reference_counts":  "s3://suching-dev/final-datasets/amazon/valid_npmi_reference/train.npz",
            "reference_vocabulary":  "s3://suching-dev/final-datasets/amazon/valid_npmi_reference/train.vocab.json",
            "stopword_path": "s3://suching-dev/stopwords/snowball_stopwords.txt",
            "glove": {
                "in-domain": "s3://suching-dev/pretrained-models/glove/amazon/vectors.txt",
                "out-domain": "https://s3-us-west-2.amazonaws.com/allennlp/datasets/glove/glove.840B.300d.txt.gz"
            },
            "elmo": {
                "frozen": "s3://allennlp/models/transformer-elmo-2019.01.10.tar.gz",
                "fine-tuned": "s3://suching-dev/pretrained-models/elmo/amazon/model.tar.gz",
                "in-domain": "s3://suching-dev/pretrained-models/in-domain-elmo/amazon/model.tar.gz"
            },
            "bert": {
                "frozen": {
                    "weights": "bert-base-uncased",
                    "vocab": "bert-base-uncased",
                },
                "fine-tuned": {
                    "weights": "s3://suching-dev/pretrained-models/bert/amazon/model.tar.gz",
                    "vocab": "s3://suching-dev/pretrained-models/bert/amazon/vocab.txt"
                }
            },
            "vae": {
                "model_archive": "s3://suching-dev/pretrained-models/vampire/amazon/small/model.tar.gz",
                "vocab": "s3://suching-dev/pretrained-models/vampire/amazon/small/vae.txt",
                "bg_freq": "s3://suching-dev/pretrained-models/vampire/amazon/small/vae.bgfreq.json"
            }

        },
        "yahoo": {
            "train": "s3://suching-dev/final-datasets/yahoo/train_pretokenized.jsonl",
            "dev": "s3://suching-dev/final-datasets/yahoo/dev_pretokenized.jsonl",
            "test": "s3://suching-dev/final-datasets/yahoo/test_pretokenized.jsonl",
            "unlabeled": "s3://suching-dev/final-datasets/yahoo/train_pretokenized.jsonl",
            "reference_counts":  "s3://suching-dev/final-datasets/yahoo/valid_npmi_reference/train.npz",
            "reference_vocabulary":  "s3://suching-dev/final-datasets/yahoo/valid_npmi_reference/train.vocab.json",
            "stopword_path": "s3://suching-dev/stopwords/snowball_stopwords.txt",
            "glove": {
                "in-domain": "s3://suching-dev/pretrained-models/glove/yahoo_300/vectors.txt",
                "out-domain": "https://s3-us-west-2.amazonaws.com/allennlp/datasets/glove/glove.840B.300d.txt.gz"
            },
            "elmo": {
                "frozen": "s3://allennlp/models/transformer-elmo-2019.01.10.tar.gz",
                "fine-tuned": "s3://suching-dev/pretrained-models/elmo/yahoo/model.tar.gz",
                "in-domain": "s3://suching-dev/pretrained-models/in-domain-elmo/yahoo/model.tar.gz"
            },
            "bert": {
                "frozen": {
                    "weights": "bert-base-uncased",
                    "vocab": "bert-base-uncased",
                },
                "fine-tuned": {
                    "weights": "s3://suching-dev/pretrained-models/bert/yahoo/model.tar.gz",
                    "vocab": "s3://suching-dev/pretrained-models/bert/yahoo/vocab.txt"
            }
        },
        "vae": {
            "model_archive": "s3://suching-dev/pretrained-models/vampire/yahoo/small_10K/model.tar.gz",
            "vocab": "s3://suching-dev/pretrained-models/vampire/yahoo/small_10K/vocabulary/vae.txt",
            "bg_freq": "s3://suching-dev/pretrained-models/vampire/yahoo/small_10K/vocabulary/vae.bgfreq.json"
        }
    },
    "hatespeech": {
        "train": "s3://suching-dev/final-datasets/hatespeech/train_pretokenized.jsonl",
        "dev": "s3://suching-dev/final-datasets/hatespeech/dev_pretokenized.jsonl",
        "test": "s3://suching-dev/final-datasets/hatespeech/test_pretokenized.jsonl",
        "unlabeled": "s3://suching-dev/final-datasets/hatespeech/train_pretokenized.jsonl",
        "reference_counts":  "s3://suching-dev/final-datasets/hatespeech/valid_npmi_reference/train.npz",
        "reference_vocabulary":  "s3://suching-dev/final-datasets/hatespeech/valid_npmi_reference/train.vocab.json",
        "stopword_path": "s3://suching-dev/stopwords/snowball_stopwords.txt",
        "glove": {
            "in-domain": "s3://suching-dev/pretrained-models/glove/hatespeech_300/vectors.txt",
            "out-domain": "https://s3-us-west-2.amazonaws.com/allennlp/datasets/glove/glove.840B.300d.txt.gz"
        },
        "elmo": {
            "frozen": "s3://allennlp/models/transformer-elmo-2019.01.10.tar.gz",
            "fine-tuned": "s3://suching-dev/pretrained-models/elmo/hatespeech/model.tar.gz",
            "in-domain": "s3://suching-dev/pretrained-models/in-domain-elmo/hatespeech/model.tar.gz"
        },
        "bert": {
            "frozen": {
                "weights": "bert-base-uncased",
                "vocab": "bert-base-uncased",
            },
            "fine-tuned": {
                "weights": "s3://suching-dev/pretrained-models/bert/hatespeech/model.tar.gz",
                "vocab": "s3://suching-dev/pretrained-models/bert/hatespeech/vocab.txt"
            }
        },
        "vae": {
            "model_archive": "s3://suching-dev/pretrained-models/vampire/hatespeech/small_10K/model.tar.gz",
            "vocab": "s3://suching-dev/pretrained-models/vampire/hatespeech/small_10K/vocabulary/vae.txt",
            "bg_freq": "s3://suching-dev/pretrained-models/vampire/hatespeech/small_10K/vocabulary/vae.bgfreq.json"
        }
    },
    "ag-news": {
        "train": "s3://suching-dev/final-datasets/ag-news/train_pretokenized.jsonl",
        "dev": "s3://suching-dev/final-datasets/ag-news/dev_pretokenized.jsonl",
        "test": "s3://suching-dev/final-datasets/ag-news/test_pretokenized.jsonl",
        "unlabeled": "s3://suching-dev/final-datasets/ag-news/train_pretokenized.jsonl",
        "reference_counts":  "s3://suching-dev/final-datasets/ag-news/valid_npmi_reference/train.npz",
        "reference_vocabulary":  "s3://suching-dev/final-datasets/ag-news/valid_npmi_reference/train.vocab.json",
        "stopword_path": "s3://suching-dev/stopwords/snowball_stopwords.txt",
        "glove": {
            "in-domain": "s3://suching-dev/pretrained-models/glove/ag-news_300/vectors.txt",
            "out-domain": "https://s3-us-west-2.amazonaws.com/allennlp/datasets/glove/glove.840B.300d.txt.gz"
        },
        "elmo": {
            "frozen": "s3://allennlp/models/transformer-elmo-2019.01.10.tar.gz",
            "fine-tuned": "s3://suching-dev/pretrained-models/elmo/ag-news/model.tar.gz",
            "in-domain": "s3://suching-dev/pretrained-models/in-domain-elmo/ag-news/model.tar.gz"
        },
        "bert": {
            "frozen": {
                "weights": "bert-base-uncased",
                "vocab": "bert-base-uncased",
            },
            "fine-tuned": {
                "weights": "s3://suching-dev/pretrained-models/bert/ag-news/model.tar.gz",
                "vocab": "s3://suching-dev/pretrained-models/bert/ag-news/vocab.txt"
            }
        },
        "vae": {
            "model_archive": "s3://suching-dev/pretrained-models/vampire/imdb/small_10K/model.tar.gz",
            "vocab": "s3://suching-dev/pretrained-models/vampire/imdb/small_10K/vocabulary/vae.txt",
            "bg_freq": "s3://suching-dev/pretrained-models/vampire/imdb/small_10K/vocabulary/vae.bgfreq.json"
        }
    },

    # Local paths for convenience.
    "imdb-local-tam": {
        "train": "/data/dangt7/datasets/final-imdb/imdb/train_tokenized.jsonl",
        "dev": "/data/dangt7/datasets/final-imdb/imdb/dev_tokenized.jsonl",
        "test": "/data/dangt7/datasets/final-imdb/imdb/test.jsonl",
        "unlabeled": "/data/dangt7/datasets/final-imdb/imdb/unlabeled_tokenized.jsonl",
        "reference_counts":  "/data/dangt7/datasets/final-imdb/imdb/valid_npmi_reference/train.npz",
        "reference_vocabulary":  "/data/dangt7/datasets/final-imdb/imdb/valid_npmi_reference/train.vocab.json",
        "stopword_path": "/home/dangt7/Research/Git/vae/vae/common/stopwords/snowball_stopwords.txt",

        # Omitting these for now.
        # "glove": "s3://suching-dev/pretrained-models/glove/imdb/vectors.txt",
        # "elmo": {
        #     "frozen": "s3://allennlp/models/transformer-elmo-2019.01.10.tar.gz",
        #     "fine-tuned": "s3://suching-dev/pretrained-models/elmo/imdb/model.tar.gz",
        #     "in-domain": "s3://suching-dev/pretrained-models/in-domain-elmo/imdb/model.tar.gz"
        # },
        # "bert": {
        #     "weights": "s3://suching-dev/pretrained-models/bert/imdb/model.tar.gz",
        #     "vocab": "s3://suching-dev/pretrained-models/bert/imdb/vocab.txt"
        # },
        "vae": {
            "model_archive": "/data/dangt7/datasets/final-imdb/imdb/pretrained_models/big/model.tar.gz",
            "vocab": "/data/dangt7/datasets/final-imdb/imdb/pretrained_models/big/vae.txt",
            "bg_freq": "/data/dangt7/datasets/final-imdb/imdb/pretrained_models/big/vae.bgfreq.json"
        }
    },
}
