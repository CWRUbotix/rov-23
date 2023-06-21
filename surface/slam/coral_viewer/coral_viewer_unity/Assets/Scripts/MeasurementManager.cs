using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class MeasurementManager : MonoBehaviour
{
    [SerializeField] GameObject diameterButton;
    [SerializeField] GameObject heightButton;
    [SerializeField] GameObject stopButton;
    [SerializeField] GameObject diameterMarker;
    [SerializeField] GameObject heightMarker;
    [SerializeField] TMP_Text diameterLabel;
    [SerializeField] TMP_Text HeightLabel; 

    int activeMeasurement = 0; // 0 = none, 1 = diameter; 2 = height

    List<GameObject> diameterMarkers = new List<GameObject>();
    List<GameObject> heightMarkers = new List<GameObject>();

    void Start()
    {
        StopMeasurement();
    }

    RaycastHit? CastRayThroughMouse()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;
        if (Physics.Raycast(ray, out hit, 100))
        {
            return hit;
        }
        return null;
    }

    void ClearMarkerList(List<GameObject> list)
    {
        foreach (GameObject marker in list)
        {
            GameObject.Destroy(marker);
        }
        list.Clear();
    }

    void UpdateDiameterText(float? diameter)
    {
        if (diameter.HasValue)
        {
            diameterLabel.text = "Coral Diameter: " + string.Format("{0:F1}", diameter.Value * 100) + " cm";
        } else
        {
            diameterLabel.text = "Coral Diameter: --";
        }
    }

    void UpdateHeightText(float? height)
    {
        if (height.HasValue)
        {
            HeightLabel.text = "Coral Height: " + string.Format("{0:F1}", height.Value * 100) + " cm";
        } else
        {
            HeightLabel.text = "Coral Height: --";
        }
    }

    void Update()
    {
        bool click = Input.GetButtonDown("Select");

        if (click) {
            foreach (GameObject button in new GameObject[] {diameterButton, heightButton, stopButton})
            {
                if (RectTransformUtility.RectangleContainsScreenPoint(button.GetComponent<RectTransform>(), Input.mousePosition))
                {
                    click = false;
                }
            }
        }

        if (click)
        {
            switch (activeMeasurement)
            {
                case 1:
                {
                    RaycastHit? hit = CastRayThroughMouse();
                    if (hit.HasValue)
                    {
                        GameObject marker = Instantiate(diameterMarker, hit.Value.point, Quaternion.identity);
                        diameterMarkers.Add(marker);

                        if (diameterMarkers.Count == 2)
                        {
                            float diameter = (diameterMarkers[1].transform.position - diameterMarkers[0].transform.position).magnitude;
                            UpdateDiameterText(diameter);
                            StopMeasurement();
                        }
                    }
                    break;
                }

                case 2:
                {
                    RaycastHit? hit = CastRayThroughMouse();
                    if (hit.HasValue)
                    {
                        GameObject marker = Instantiate(heightMarker, hit.Value.point, Quaternion.identity);
                        heightMarkers.Add(marker);

                        if (heightMarkers.Count == 4)
                        {
                            Vector3 planeNormal = Vector3.Cross(heightMarkers[1].transform.position - heightMarkers[0].transform.position, heightMarkers[2].transform.position - heightMarkers[0].transform.position);
                            float distance = Math.Abs(Vector3.Project(heightMarkers[3].transform.position - heightMarkers[0].transform.position, planeNormal).magnitude);
                            UpdateHeightText(distance);
                            StopMeasurement();
                        }
                    }
                    break;
                }
            }
        }
    }

    public void StartDiameterMeasurement()
    {
        activeMeasurement = 1;
        stopButton.SetActive(true);
        ClearMarkerList(diameterMarkers);
    }

    public void StartHeightMeasurement()
    {
        activeMeasurement = 2;
        stopButton.SetActive(true);
        ClearMarkerList(heightMarkers);
    }

    public void StopMeasurement()
    {
        activeMeasurement = 0;
        stopButton.SetActive(false);

        if (diameterMarkers.Count != 2)
        {
            ClearMarkerList(diameterMarkers);
        }

        if (heightMarkers.Count != 4)
        {
            ClearMarkerList(heightMarkers);
        }
    }
}
