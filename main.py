import structlog


def main():
    structlog.configure(
        processors=[structlog.processors.JSONRenderer(ensure_ascii=False)]
    )
    log = structlog.getLogger("my-logger")
    log.info("こんにちは", hoge="ほげ")


if __name__ == "__main__":
    main()
