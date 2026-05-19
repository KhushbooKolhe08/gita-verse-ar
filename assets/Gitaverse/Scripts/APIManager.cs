using System.Collections;
using UnityEngine;
using UnityEngine.Networking;
using TMPro;
using System.Text;

public class APIManager : MonoBehaviour
{
    public TMP_InputField questionInput;
    public TMP_Text answerText;

    private string apiURL = "http://127.0.0.1:8000/ask";

    [System.Serializable]
    public class QuestionData
    {
        public string question;
    }

    [System.Serializable]
    public class ResponseData
    {
        public string answer;
    }

    public void AskQuestion()
    {
        StartCoroutine(SendQuestion());
    }

    IEnumerator SendQuestion()
    {
        QuestionData data = new QuestionData();

        data.question = questionInput.text;

        string jsonData = JsonUtility.ToJson(data);

        UnityWebRequest request =
            new UnityWebRequest(apiURL, "POST");

        byte[] bodyRaw = Encoding.UTF8.GetBytes(jsonData);

        request.uploadHandler =
            new UploadHandlerRaw(bodyRaw);

        request.downloadHandler =
            new DownloadHandlerBuffer();

        request.SetRequestHeader(
            "Content-Type",
            "application/json"
        );

        yield return request.SendWebRequest();

        if(request.result ==
            UnityWebRequest.Result.Success)
        {
            ResponseData response =
                JsonUtility.FromJson<ResponseData>(
                    request.downloadHandler.text
                );

            answerText.text =
                response.answer;
        }
        else
        {
            answerText.text =
                request.error;
        }
    }
}