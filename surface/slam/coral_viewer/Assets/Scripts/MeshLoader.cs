using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using UnityEngine;

public class MeshLoader : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Mesh mesh = new Mesh();

        using (StreamReader reader = new StreamReader(Path.Join(Application.streamingAssetsPath, "coral_output.obj.txt")))
        {
            string line;
            int lineCount = 0;
            int phase = 0; // 0 = comments, 1 = verticies and normals, 2 = faces

            List<Vector3> verticies = new List<Vector3>();
            List<Vector3> normals = new List<Vector3>();
            List<int> triangles = new List<int>();
            List<Color> colors = new List<Color>();

            Regex vertexRegex = new Regex("v ([\\d.e\\-]+) ([\\d.e\\-]+) ([\\d.e\\-]+) ([\\d.e\\-]+) ([\\d.e\\-]+) ([\\d.e\\-]+)");
            Regex normalRegex = new Regex("vn ([\\d.e\\-]+) ([\\d.e\\-]+) ([\\d.e\\-]+)");
            Regex faceRegex = new Regex("f (\\d+)\\/\\/\\d+ (\\d+)\\/\\/\\d+ (\\d+)\\/\\/\\d+");

            while ((line = reader.ReadLine()) != null)
            {
                switch (line[0])
                {
                    case 'v':
                        phase = 1;
                        break;
                    case 'f':
                        phase = 2;
                        break;
                }

                switch (phase)
                {
                    case 0:
                        // Line is a comment, pass
                        break;

                    case 1:
                        if (line[1] == ' ')
                        {
                            // Line specifies a vertex and its color
                            Match m = vertexRegex.Match(line);
                            verticies.Add(new Vector3(float.Parse(m.Groups[1].Value), float.Parse(m.Groups[2].Value), float.Parse(m.Groups[3].Value)));
                            colors.Add(new Color(float.Parse(m.Groups[4].Value), float.Parse(m.Groups[5].Value), float.Parse(m.Groups[6].Value), 1f));
                        } else
                        {
                            // Line specifies a vertex normal
                            Match m = normalRegex.Match(line);
                            normals.Add(new Vector3(float.Parse(m.Groups[1].Value), float.Parse(m.Groups[2].Value), float.Parse(m.Groups[3].Value)));
                        }
                        break;

                    case 2:
                        Match triMatch = faceRegex.Match(line);
                        triangles.Add(Int32.Parse(triMatch.Groups[1].Value) - 1);
                        triangles.Add(Int32.Parse(triMatch.Groups[2].Value) - 1);
                        triangles.Add(Int32.Parse(triMatch.Groups[3].Value) - 1);
                        break;
                }

                lineCount++;
            }

            mesh.SetVertices(verticies);
            mesh.SetNormals(normals);
            mesh.SetColors(colors);
            mesh.SetTriangles(triangles, 0);

            GetComponent<MeshFilter>().mesh = mesh;
            GetComponent<MeshCollider>().sharedMesh = mesh;
        }

    }
}
