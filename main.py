import json
import structlog


def dumps_allow_non_ascii(obj, **kwargs) -> str | bytes:
    new_kwars = kwargs | {"ensure_ascii": False}
    return json.dumps(obj, **new_kwars)


def main():
    structlog.configure(
        processors=[structlog.processors.JSONRenderer(serializer=dumps_allow_non_ascii)]
    )
    log = structlog.getLogger("my-logger")
    log.info("こんにちは", hoge="ほげ")


if __name__ == "__main__":
    main()
