import { useMemo } from "react";

function ImageUploader({ image, onImageChange }) {
    const preview = useMemo(() => {
        if (!image) {
            return null;
        }

        return URL.createObjectURL(image);
    }, [image]);

    const handleImageChange = (event) => {
        const file = event.target.files[0];

        if (file) {
            onImageChange(file);
        }

        // Allows selecting the same file again after removing it
        event.target.value = "";
    };

    const handleRemove = () => {
        onImageChange(null);
    };

    const formatFileSize = (bytes) => {
        if (bytes < 1024 * 1024) {
            return `${(bytes / 1024).toFixed(1)} KB`;
        }

        return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;
    };

    return (
        <div className="mt-6">
            <input
                id="sampleImage"
                type="file"
                accept="image/png,image/jpeg"
                onChange={handleImageChange}
                className="hidden"
            />

            {!image ? (
                <label
                    htmlFor="sampleImage"
                    className="flex min-h-72 cursor-pointer flex-col items-center justify-center rounded-xl border-2 border-dashed border-slate-300 bg-slate-50 px-6 text-center transition hover:border-teal-400 hover:bg-teal-50/30"
                >
                    <div className="flex h-14 w-14 items-center justify-center rounded-full bg-teal-100 text-2xl">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            strokeWidth="1.5"
                            stroke="currentColor"
                            className="h-7 w-7 text-teal-600"
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                d="M6.827 6.175A2.31 2.31 0 0 1 5.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 0 0-1.134-.175 2.31 2.31 0 0 1-1.64-1.055l-.822-1.316a2.192 2.192 0 0 0-1.736-1.039 48.774 48.774 0 0 0-5.232 0 2.192 2.192 0 0 0-1.736 1.039l-.821 1.316Z"
                            />
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                d="M16.5 12.75a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0ZM18.75 10.5h.008v.008h-.008V10.5Z"
                            />
                        </svg>
                    </div>

                    <p className="mt-4 text-sm font-semibold text-slate-900">
                        Upload sample image
                    </p>

                    <p className="mt-1 text-sm text-slate-500">
                        PNG or JPEG
                    </p>

                    <span className="mt-4 rounded-lg bg-white px-4 py-2 text-sm font-medium text-slate-700 shadow-sm ring-1 ring-slate-200">
            Browse image
          </span>
                </label>
            ) : (
                <div className="overflow-hidden rounded-xl border border-slate-200 bg-white">

                    {/* Image preview */}
                    <div className="relative flex min-h-72 items-center justify-center bg-slate-100 p-4">
                        <img
                            src={preview}
                            alt="Sample preview"
                            className="max-h-96 max-w-full rounded-lg object-contain"
                        />
                    </div>

                    {/* File information */}
                    <div className="flex items-center justify-between border-t border-slate-200 p-4">

                        <div className="min-w-0">
                            <p className="truncate text-sm font-medium text-slate-900">
                                {image.name}
                            </p>

                            <p className="mt-1 text-xs text-slate-500">
                                {formatFileSize(image.size)}
                            </p>
                        </div>

                        <div className="ml-4 flex shrink-0 gap-2">

                            <label
                                htmlFor="sampleImage"
                                className="cursor-pointer rounded-lg border border-slate-200 px-3 py-2 text-sm font-medium text-slate-600 transition hover:bg-slate-50"
                            >
                                Change
                            </label>

                            <button
                                type="button"
                                onClick={handleRemove}
                                className="rounded-lg px-3 py-2 text-sm font-medium text-red-600 transition hover:bg-red-50"
                            >
                                Remove
                            </button>

                        </div>

                    </div>
                </div>
            )}
        </div>
    );
}

export default ImageUploader;