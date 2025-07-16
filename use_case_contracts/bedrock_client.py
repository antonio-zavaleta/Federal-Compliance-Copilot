import boto3
import json
from botocore.exceptions import ClientError

def invoke_claude_3(prompt):
    """
    Invokes the Anthropic Claude 3 Haiku model to run an inference.
    """
    # Initialize the client
    session = boto3.Session(profile_name="arica-llm-bridger")
    client = session.client("bedrock-runtime", region_name="us-east-1")
    model_id = "anthropic.claude-3-haiku-20240307-v1:0"

    # Create the native request body
    native_request = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.5,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
    }
    request = json.dumps(native_request)

    try:
        # Invoke the model
        response = client.invoke_model(modelId=model_id, body=request)
        model_response = json.loads(response["body"].read())
        response_text = model_response["content"][0]["text"]
        return response_text

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        exit(1)


# To test the function directly
if __name__ == "__main__":
    test_prompt = "Describe the purpose of a 'hello world' program in one line."
    response = invoke_claude_3(test_prompt)
    print(response)