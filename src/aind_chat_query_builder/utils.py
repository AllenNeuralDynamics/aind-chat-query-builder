"""Script to initialize tools and agents"""

from aind_data_access_api.document_db import MetadataDbClient
from langchain_aws.chat_models.bedrock import ChatBedrockConverse

API_GATEWAY_HOST = "api.allenneuraldynamics.org"
docdb_client_v1 = MetadataDbClient(host=API_GATEWAY_HOST)
docdb_client_v2 = MetadataDbClient(host=API_GATEWAY_HOST, version="v2")

BEDROCK_SONNET_4 = "us.anthropic.claude-sonnet-4-20250514-v1:0"
SONNET_4_LLM = ChatBedrockConverse(
    model=BEDROCK_SONNET_4,
    temperature=0,
)


def get_records(filter: dict = {}) -> dict:
    """
    Retrieves documents from MongoDB database using simple filters
    and projections.

    WHEN TO USE THIS FUNCTION:
    - For straightforward document retrieval based on specific criteria
    - When you need only a subset of fields from documents
    - When the query logic doesn't require multi-stage processing
    - For better performance with simpler queries

    NOT RECOMMENDED FOR:
    - Complex data transformations (use aggregation_retrieval instead)
    - Grouping operations or calculations across documents
    - Joining or relating data across collections

    Parameters
    ----------
    filter : dict
        MongoDB query filter to narrow down the documents to retrieve.
        Example: {"subject.sex": "Male"}
        If empty dict object, returns all documents.

    Returns
    -------
    list
        List of dictionary objects representing the matching documents.
        Each dictionary contains the requested fields based on the projection.

    """

    records = docdb_client_v1.retrieve_docdb_records(filter_query=filter)

    return records


def aggregation_retrieval(agg_pipeline: list):
    """
    Executes a MongoDB aggregation pipeline for complex data transformations
    and analysis.

    WHEN TO USE THIS FUNCTION:
    - When you need to perform multi-stage data processing operations
    - For complex queries requiring grouping, filtering, sorting in sequence
    - When you need to calculate aggregated values (sums, averages, counts)
    - For data transformation operations that can't be done with simple queries

    NOT RECOMMENDED FOR:
    - Simple document retrieval (use get_records instead)
    - When you only need to filter data without transformations
    Executes a MongoDB aggregation pipeline and returns the aggregated results.

    This function processes complex queries using MongoDB's aggregation
    framework, allowing for data transformation, filtering, grouping, and
    analysis operations. It handles the execution of multi-stage aggregation
    pipelines and provides error handling for failed aggregations.

    Parameters
    ----------
    agg_pipeline : list
        A list of dictionary objects representing MongoDB aggregation stages.
        Each stage should be a valid MongoDB aggregation operator.
        Common stages include: $match, $project, $group, $sort, $unwind.

    Returns
    -------
    list
        Returns a list of documents resulting from the aggregation pipeline.
        If an error occurs, returns an error message string describing
        the exception.

    Notes
    -----
    - Include a $project stage early in the pipeline to reduce data transfer
    - Avoid using $map operator in $project stages as it requires array inputs
    """
    result = docdb_client_v2.aggregate_docdb_records(pipeline=agg_pipeline)

    return result


simple_tools = [get_records]
complex_tools_v2 = [aggregation_retrieval]

simple_agent = SONNET_4_LLM.bind_tools(simple_tools)
complex_agent_v2 = SONNET_4_LLM.bind_tools(complex_tools_v2)
