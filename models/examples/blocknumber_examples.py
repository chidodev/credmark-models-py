#pylint: disable=pointless-string-statement, pointless-statement

import credmark.model
from credmark.types.data.block_number import BlockNumberOutOfRangeError, BlockNumber
from credmark.model.errors import ModelRunError


@credmark.model.describe(slug='example.block-number',
                         version='1.0',
                         display_name='(Example) BlockNumber',
                         description='This example shows the capabilities on the BlockNumber class',
                         input=dict,
                         output=dict)
class BlockNumberTransformExample(credmark.model.Model):

    """
    This example shows the capabilities on the BlockNumber class
    """

    def run(self, input) -> dict:

        block_number = self.context.block_number
        self.logger.info(
            f"block_number : {block_number}")
        self.logger.info(
            f"block_number.timestamp : {block_number.timestamp}")
        self.logger.info(
            f"block_number.timestamp_datetime : {block_number.timestamp_datetime}")
        self.logger.info(
            f"(block_number - 1000) : {(block_number - 1000)}")
        self.logger.info(
            f"(block_number - 1000).timestamp_datetime : {(block_number - 1000).timestamp_datetime}")  # pylint: disable=line-too-long
        self.logger.info(
            f"block_number.from_datetime(block_number.timestamp - 3600): {block_number.from_timestamp(block_number.timestamp - 3600)}")  # pylint: disable=line-too-long
        self.logger.info(
            f"BlockNumber.from_datetime(block_number.timestamp - 3600): {BlockNumber.from_timestamp(block_number.timestamp - 3600)}")  # pylint: disable=line-too-long
        """
            NOTE: THIS IS FOR DEMONSTRATION ONLY.
            You should NOT catch BlockNumberOutOfRangeError or
            other ModelRunErrors in your models!
        """
        try:
            block_number + 1000000  # type: ignore
            raise ModelRunError(
                message='BlockNumbers cannot exceed the current context.block_number, '
                'an exception was NOT caught, and the example has FAILED')
        except BlockNumberOutOfRangeError as _e:
            self.logger.info(_e)
<<<<<<< HEAD
            self.logger.info("Attempting to create a BlockNumber object higher than the current "
                             "context's block_number raises BlockNumberOutOfRangeError")
=======
            self.logger.info(
                "Attempting to create a BlockNumber object higher than the current context's block_number raises BlockNumberOutOfRangeError")
>>>>>>> 42271ec (example cleanup)

        try:
            BlockNumber(-1)
            raise ModelRunError(
                message="BlockNumbers cannot be negative, an exception was NOT caught, "
                "and the example has FAILED")
        except BlockNumberOutOfRangeError as _e:
            self.logger.info(_e)
            self.logger.info(
                "Attempting to create a BlockNumber object with a negative block number "
                "raises BlockNumberOutOfRangeError")

        return dict(block_number=block_number)
