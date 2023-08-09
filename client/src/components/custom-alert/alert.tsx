type AlertProps = {
  type?: 'success' | 'danger';
  data: string | string[];
};

export default function Alert({ type = 'success', data }: AlertProps) {
  return (
    <div className={`alert alert-${type}`}>
      {Array.isArray(data) ? (
        <ul className="list-unstyled">
          {data.map((d, i) => (
            <li key={i}>{d}</li>
          ))}
        </ul>
      ) : (
        data
      )}
    </div>
  );
}
