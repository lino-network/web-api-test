

def login(username, password):
    payload = {
        "operationName": "EmailLogin",
        "variables": {
            "email": username,
            "password": password,
            "recaptchaToken": "03AL8dmw8ysn8ewYpObge7klDuBHutVNnLIy9yfcbxPw9m8HpYuyQ_R7t_IWhBEP3fuV6ZGkq_Uv8a621oADJ6XlJxMjCojJWkY_rkDuXfr3jhZ53uPl7dQS3Q9k3sNvYeTYcrIGsLz8H-34SL__KJ1AAgRlhAYtM_4e1HzVnYTbNAaMvIK-6Qti38XsHNUXpGn9Fmkm3KLlcvOwI2kx95Wft8fFUCvz1ccopRI4NwxOLe_3Aa5MiokU2YcTX-bUjJ1XI_O0m6YtXhh9ieeI3yQCXpSph2NUb5h9g-dz_gGoHhVjBFa52Gp7vCZjqxkg7Jxw3GlTMKjivR-MjaHPhBxW1n3F8MQ84TpLJo4Y4UsXk-oEM04g7g47nNOi2kG3lU6FWTSYR8lzDTIz1OKeptr0jfQuuhAQ0QhQByVCORuTGQhrHpQ8LaGeaU30eaWkC9XvPBXriVjW22mMjZ1iYF7Zrj1d9S-sHXe5CCxlPVe5tFg4d5yTvUwvsc3x8rrbU9qjPXQtdzf60JLkEK9r-4OnzpwE-TXBvra_WeD8XIx5JaKPL7FLjIKkt5U9SHG_6kTbEdeeD0FJiG"
           # "recaptchaToken": "03AL8dmw9MnDH_La_lUO2gjCrh5vSjqAWFJHHx_t84rj1v7lum-kGTKUmxIMqMB2OwQ6n1EXLFEwE9tvriY7x1Yxvig7RHHXXUSjHV32KATS2nBrB-Qvl_wzHGEDLoUvIW5S_PmgvlWMJA7ouc1m8FTwkRA-x0jbp0dENUP9mmL6ugCWZuw8dIH_Im9cc--GGQbpwz4z4p5pIWATd4LGmaqkIpfk2L-_6wusqPun0GN9zqprwOzn1aREuH4YhLCPx2ry-JVvlvgR7HgTMCxktPAbg2c59phmASqH72XZEPW8u8Slzfn8FxKI37zj0wk7sB4v_1JBcvykxtWEYrTyzZF4833Y6i75Ehct5S2NYAStCJAwhZOyvWkPqwZBLjpj_LYw6Ib6XP7dQn86AgxMUZPqdZ2lZ6SIIuM5kCthPcfo8hT4MdjNbEObzmcdMXrqmmVbOQ9YYZIRaQAHB6zrYJ49lYczLMb0Ngj3hE6Jpi7SY3EFssXhOR_R0r5ls-IWu0CaUyw0IDbc5lulLQKHMjSUDVKQtPic_Bbc-4TEGQdLTQxKolWvEZIbY"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "ee5f1abab8122a4441ed378b01f0905612ce3e053c80c1eb1f15cd28310ff017"
            }
        }
    }
    return payload


def follow_user(userId):
    payload = {
        "operationName": "FollowUser",
        "variables": {
            "streamer": userId
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "daf146d77e754b6b5a7acd945ff005ae028b33feaa3c79e04e71505190003a5d"
            }
        }
    }
    return payload


def sidebar_follow_user_list():
    payload = {
        "operationName": "MeSidebar",
        "variables": {
            "folowingFirst": 500,
            "after": "MeSidebar"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "14cff202984215984934df214bacf048befd9d8dc21791b0391ce65bd2981484"
            }
        }
    }

    return payload

