using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class DialogueSystem : MonoBehaviour
{
    public TextMeshProUGUI txtName, txtSentence;

    Queue<string> names = new Queue<string>();
    Queue<string> sentences = new Queue<string>();

    public void Begin(Dialogue info)
    {
        sentences.Clear();

        foreach (var name in info.names)
        {
            names.Enqueue(name);
        }
        foreach (var sentence in info.sentences)
        {
            sentences.Enqueue(sentence);
        }

        Next();

    }

    public void Next()
    {
        if(sentences.Count == 0)End();
            txtName.text = names.Dequeue();
            txtSentence.text = sentences.Dequeue();

            return;
    }

    private void End()
    {
        Debug.Log("End of Chapter");
    }

}
