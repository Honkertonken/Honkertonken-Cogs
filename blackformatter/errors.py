class NoData(Exception):
    """
    No argument or file was passed.
    """


class AttachmentPermsError(NoData):
    """
    Can't access attachment.
    """


class AttachmentInvalid(NoData):
    """
    Attachment has wrong file type.
    """
