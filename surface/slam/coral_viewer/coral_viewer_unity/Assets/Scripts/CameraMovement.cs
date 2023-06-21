using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;

public class CameraMovement : MonoBehaviour
{
    public float panSensitivity;
    public float orbitSensitivity;
    public float zoomSensistivity;

    void Update()
    {
        bool panDown = Input.GetButton("Pan");
        bool orbitDown = Input.GetButton("Orbit");
        Vector2 mouseDelta = new Vector2(Input.GetAxis("Mouse X"), Input.GetAxis("Mouse Y"));
        
        if (orbitDown)
        {
            this.transform.Rotate(new Vector3(-mouseDelta.y * orbitSensitivity, mouseDelta.x * orbitSensitivity, 0), Space.Self);
        } else if (panDown)
        {
            this.transform.Translate(new Vector3(-mouseDelta.x * panSensitivity, -mouseDelta.y * panSensitivity, 0) * this.transform.localScale.z, Space.Self);
        }

        float mouseScroll = Input.GetAxis("Mouse ScrollWheel");
        this.transform.localScale *= (float)Math.Pow(2.0, -mouseScroll);
    }
}
