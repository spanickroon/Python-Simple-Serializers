#!.venv/bin/python3
from formatserializer.args.arguments import ConvertArguments
from formatserializer.converters.format_converter import FormatConverter


def main():
    parser = ConvertArguments().setup_args()

    ConvertArguments.parsing_config_file(parser)

    converter = FormatConverter(
        convert_format=parser.convert_format,
        file_from_covert=parser.file_from_convert,
        file_to_convert=parser.file_to_convert
    )

    converter.convert()


if __name__ == "__main__":
    main()
