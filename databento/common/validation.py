from enum import Enum
from typing import Optional, Type, TypeVar, Union
from urllib.parse import urlsplit, urlunsplit


E = TypeVar("E", bound=Enum)


def validate_enum(
    value: object,
    enum: Type[E],
    param: str,
) -> E:
    """
    Validate whether the given value is either the correct Enum type, or a valid
    value of that enum.

    Parameters
    ----------
    value : Enum or str, optional
        The value to validate.
    enum : Type[Enum]
        The valid enum type.
    param : str
        The name of the parameter being validated (for any error message).

    Returns
    -------
    Enum
        A valid member of Enum.

    Raises
    ------
    ValueError
        If value is not valid for the given enum.

    """
    try:
        return enum(value)
    except ValueError as exc:
        valid = tuple(map(str, enum))
        raise ValueError(
            f"The `{param}` was not a valid value of {enum}, was '{value}'. "
            f"Use any of {valid}.",
        ) from exc


def validate_maybe_enum(
    value: Optional[Union[E, str]],
    enum: Type[E],
    param: str,
) -> Optional[E]:
    """
    Validate whether the given value is either the correct Enum type, a valid
    value of that enum, or None.

    Parameters
    ----------
    value : Enum or str, optional
        The value to validate.
    enum : Type[Enum]
        The valid enum type.
    param : str
        The name of the parameter being validated (for any error message).

    Returns
    -------
    Enum or None
        A valid member of Enum or None.

    Raises
    ------
    ValueError
        If value is not valid for the given enum.

    """
    if value is None:
        return None
    return validate_enum(value, enum, param)


def validate_gateway(
    url: str,
) -> str:
    """
    Validate that the given value is a valid gateway URL.

    Parameters
    ----------
    url : str
        The URL to validate

    Returns
    -------
    str
        The gateway URL if it is valid.

    Raises
    ------
    ValueError
        If the URL is invalid.

    """
    url_chunks = urlsplit(url)

    if not any([url_chunks.netloc, url_chunks.path]):
        raise ValueError(f"`{url}` is not a valid URL")

    if url_chunks.netloc:
        return urlunsplit(
            components=("https", url_chunks.netloc, url_chunks.path, "", ""),
        )
    return urlunsplit(components=("https", url_chunks.path, "", "", ""))
