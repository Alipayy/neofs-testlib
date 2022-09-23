from neofs_testlib.cli.cli_command import CliCommand
from neofs_testlib.shell import CommandResult


class NeoGoQuery(CliCommand):
    def candidates(
        self,
        rpc_endpoint: str,
        timeout: int = 10,
    ) -> CommandResult:
        """Get candidates and votes

        Args:
            rpc_endpoint (str):  RPC node address
            timeout (int):       Timeout for the operation (default: 10s)

        Returns:
            str: Command string

        """
        return self._execute(
            "query candidates",
            **{
                param: param_value
                for param, param_value in locals().items()
                if param not in ["self"]
            },
        )

    def committee(
        self,
        rpc_endpoint: str,
        timeout: int = 10,
    ) -> CommandResult:
        """Get committee list

        Args:
            rpc_endpoint (str):  RPC node address
            timeout (int):       Timeout for the operation (default: 10s)

        Returns:
            str: Command string

        """
        return self._execute(
            "query committee",
            **{
                param: param_value
                for param, param_value in locals().items()
                if param not in ["self"]
            },
        )

    def height(
        self,
        rpc_endpoint: str,
        timeout: int = 10,
    ) -> CommandResult:
        """Get node height

        Args:
            rpc_endpoint (str):  RPC node address
            timeout (int):       Timeout for the operation (default: 10s)

        Returns:
            str: Command string

        """
        return self._execute(
            "query height",
            **{
                param: param_value
                for param, param_value in locals().items()
                if param not in ["self"]
            },
        )

    def tx(
        self,
        tx_hash: str,
        rpc_endpoint: str,
        timeout: int = 10,
    ) -> CommandResult:
        """Query transaction status

        Args:
            tx_hash (str):       Hash of transaction
            rpc_endpoint (str):  RPC node address
            timeout (int):       Timeout for the operation (default: 10s)

        Returns:
            str: Command string

        """
        return self._execute(
            f"query tx {tx_hash}",
            **{
                param: param_value
                for param, param_value in locals().items()
                if param not in ["self", "hash"]
            },
        )

    def voter(
        self,
        rpc_endpoint: str,
        timeout: int = 10,
    ) -> CommandResult:
        """Print NEO holder account state

        Args:
            rpc_endpoint (str):  RPC node address
            timeout (int):       Timeout for the operation (default: 10s)

        Returns:
            str: Command string

        """
        return self._execute(
            "query voter",
            **{
                param: param_value
                for param, param_value in locals().items()
                if param not in ["self"]
            },
        )