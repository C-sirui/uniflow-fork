"""Extract PDF Flow."""

from typing import Any, Dict, Sequence

from uniflow.constants import EXTRACT
from uniflow.flow.flow import Flow
from uniflow.node.node import Node
from uniflow.op.extract.load.pdf_op import ProcessPDFOp
from uniflow.op.model.model_op import LLMDataPreprocessor


class ExtractPDFFlow(Flow):
    """Extract PDF Flow Class."""

    TAG = EXTRACT

    def __init__(
        self,
        model_config: Dict[str, Any],
    ) -> None:
        """HuggingFace Model Flow Constructor.

        Args:
            model_server (str): Model server name.
            few_shot_template (Dict[str, Any]): Few shot template.
            model_config (Dict[str, Any]): Model config.
        """
        super().__init__()
        self._process_pdf_op = ProcessPDFOp(
            name="process_pdf_op",
            model=LLMDataPreprocessor(
                model_config=model_config,
            ),
        )

    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run Model Flow.

        Args:
            nodes (Sequence[Node]): Nodes to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        return self._process_pdf_op(nodes)
