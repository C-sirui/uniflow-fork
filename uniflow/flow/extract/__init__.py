"""Model __init__ Module."""

# this register all possible model server into ModelServerFactory through
# ModelServerFactory.register(cls.__name__, cls) in AbsModelServer
# __init_subclass__

from uniflow.flow.extract.extract_pdf_flow import ExtractPDFFlow  # noqa: F401;
from uniflow.flow.extract.extract_txt_flow import \
    ExtractTxtFlow  # noqa: F401, F403

__all__ = ["ExtractTxtFlow", "ExtractPDFFlow"]
