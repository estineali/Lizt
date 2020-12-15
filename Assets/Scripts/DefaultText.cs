using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class DefaultText : MonoBehaviour
{
    [SerializeField]
    TMP_FontAsset defaultFont;

    public TMP_FontAsset DefaultFont
    {
        get {return defaultFont;}
    }

    private void Start()
    {
        TextMeshProUGUI[] textObjects = GetComponents<TextMeshProUGUI>();

        foreach (TextMeshProUGUI textObject in textObjects)
        {
            textObject.font = defaultFont;
        }
    }

}

